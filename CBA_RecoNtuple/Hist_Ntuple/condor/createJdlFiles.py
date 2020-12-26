import itertools
import os
from HistInputs import *

if not os.path.exists("tmpSub/log"):
    os.makedirs("tmpSub/log")
condorLogDir = "log"
tarFile = "tmpSub/Hist_Ntuple.tar.gz"
if os.path.exists(tarFile):
	os.system("rm %s"%tarFile)
os.system("tar -zcvf %s ../../Hist_Ntuple --exclude condor"%tarFile)
os.system("cp runMakeHists.sh tmpSub/")
common_command = \
'Universe   = vanilla\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
Transfer_Input_Files = Hist_Ntuple.tar.gz, runMakeHists.sh\n\
use_x509userproxy = true\n\
Output = %s/log_$(cluster)_$(process).stdout\n\
Error  = %s/log_$(cluster)_$(process).stderr\n\
Log    = %s/log_$(cluster)_$(process).condor\n\n'%(condorLogDir, condorLogDir, condorLogDir)

#----------------------------------------
#Create jdl files
#----------------------------------------
subFile = open('tmpSub/condorSubmit.sh','w')
for year, decay, channel in itertools.product(Year, Decay, Channel):
    condorOutDir = "%s/%s/%s/%s"%(condorHistDir, year, decay, channel)
    os.system("eos root://cmseos.fnal.gov mkdir -p %s"%condorOutDir)
    jdlName = 'submitJobs_%s%s%s.jdl'%(year, decay, channel)
    jdlFile = open('tmpSub/%s'%jdlName,'w')
    jdlFile.write('Executable =  runMakeHists.sh \n')
    jdlFile.write(common_command)
    if channel=="Mu": 
        Samples.remove("QCDEle")
        Samples.remove("DataEle")
    else: 
        Samples.remove("QCDMu")
        Samples.remove("DataMu")
    
    #Create for Base, Signal region
    for sample in Samples:
        run_command =  \
		'arguments  = %s %s %s %s \n\
queue 1\n\n' %(year, decay, channel, sample)
	jdlFile.write(run_command)
    
    #Create for Base, Control region
    for sample, cr in itertools.product(Samples, ControlRegion):
        run_command =  \
		'arguments  = %s %s %s %s %s \n\
queue 1\n\n' %(year, decay, channel, sample, cr)
	jdlFile.write(run_command)
	
    #Create for Syst, Signal region
    for sample, syst, level in itertools.product(Samples, Systematics, SystLevel):
        run_command =  \
		'arguments  = %s %s %s %s %s %s \n\
queue 1\n\n' %(year, decay, channel, sample, syst, level)
        if not sample in ["DataMu", "DataEle", "QCD_DD"]:
            jdlFile.write(run_command)
    
    #Create for Syst, Control region
    for sample, syst, level, cr in itertools.product(Samples, Systematics, SystLevel, ControlRegion):
        run_command =  \
		'arguments  = %s %s %s %s %s %s %s \n\
queue 1\n\n' %(year, decay, channel, sample, syst, level, cr)
        if not sample in ["DataMu", "DataEle", "QCD_DD"]:
            jdlFile.write(run_command)
	#print "condor_submit jdl/%s"%jdlFile
    subFile.write("condor_submit %s\n"%jdlName)
    jdlFile.close() 
    if channel=="Mu": 
        Samples.append("QCDEle")
        Samples.append("DataEle")
    else: 
        Samples.append("QCDMu")
        Samples.append("DataMu")
subFile.close()
