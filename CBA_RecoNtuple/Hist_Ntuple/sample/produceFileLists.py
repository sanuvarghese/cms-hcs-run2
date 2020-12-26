import os
import sys
import subprocess

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("CBA_RecoNtuple/Hist_Ntuple/sample","Skim_NanoAOD/sample"))
from NanoAOD_Gen_SplitJobs_cff import Samples_2016, Samples_2017, Samples_2018
eosDir = "/store/user/rverma/Output/cms-hcs-run2/RecoNtuple_Skim" 
#for year in [2016]:
skimFiles = open('RecoNtuple_Skim_FileLists_cff.py','w')
for year in [2016,2017,2018]:
    print  "------------: %s :-----------"%year 
    print  "Sub\t  Done\t Diff\t Sample"
    missingJobs = {}
    line = ""
    sampleList = eval("Samples_%i"%year)
    for sampleName, nJob in sampleList.items():
        line += "%s_%s"%(sampleName,year) 
        #line += sampleName
        extraArgs = "%s_RecoNtuple_Skim*.root"%sampleName
        fileList = subprocess.Popen('eos root://cmseos.fnal.gov/ ls %s/%i/%s'%(eosDir, year, extraArgs),shell=True,stdout=subprocess.PIPE).communicate()[0].split('\n')
        fileList.remove("")
        nFiles = len(fileList)
        allFiles = []
        for f in fileList:
            allFiles.append(str(f).split("/")[-1])
        line += " = "
        line += str(allFiles)
        line += '\n\n'
        print("%i\t %i\t %i\t %s"%(nJob, nFiles, nJob-nFiles, sampleName))
        if nFiles is not nJob:
            missingJobs[sampleName] = nJob -nFiles
    skimFiles.write(line.encode('ascii'))
    print "Missing jobs:", missingJobs
skimFiles.close()

