import itertools
import os
import sys

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("condor","sample"))
from AllSamples_2016 import sampleList_2016
from AllSamples_2017 import sampleList_2017
from AllSamples_2018 import sampleList_2018

if not os.path.exists("tmpSub/log"):
    os.makedirs("tmpSub/log")
condorLogDir = "log"
tarFile = "tmpSub/Skim-NanoAOD.tar.gz"
if os.path.exists(tarFile):
	os.system("rm %s"%tarFile)
os.system("tar -zcvf %s ../../Skim-NanoAOD --exclude condor"%tarFile)
os.system("cp runMakeSkims.sh tmpSub/")
common_command = \
'Universe   = vanilla\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
Transfer_Input_Files = Skim-NanoAOD.tar.gz, runMakeSkims.sh\n\
use_x509userproxy = true\n\
Output = %s/log_$(cluster)_$(process).stdout\n\
Error  = %s/log_$(cluster)_$(process).stderr\n\
Log    = %s/log_$(cluster)_$(process).condor\n\n'%(condorLogDir, condorLogDir, condorLogDir)

#----------------------------------------
#Create jdl files
#----------------------------------------
subFile = open('tmpSub/condorSubmit.sh','w')
for year in [2016,2017,2018]:
    sampleList = eval("sampleList_%i"%year)
    jdlName = 'submitJobs_%s.jdl'%(year)
    jdlFile = open('tmpSub/%s'%jdlName,'w')
    jdlFile.write('Executable =  runMakeSkims.sh \n')
    jdlFile.write(common_command)
    condorOutDir="/store/user/rverma/Output/cms-hcs-run2/Skim-NanoAOD"
    os.system("eos root://cmseos.fnal.gov mkdir -p %s/%s"%(condorOutDir, year))
    
    for sampleName in sampleList.keys():
        run_command =  'Arguments  = %s %s \nQueue 1\n\n' %(year, sampleName)
	jdlFile.write(run_command)
    
	#print "condor_submit jdl/%s"%jdlFile
    subFile.write("condor_submit %s\n"%jdlName)
    jdlFile.close() 
subFile.close()
