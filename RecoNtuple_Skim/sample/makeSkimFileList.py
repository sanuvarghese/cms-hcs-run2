import os
import sys
import subprocess

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("RecoNtuple_Skim/sample","Skim_NanoAOD/sample"))
from NanoAOD_Gen_Samples_2016 import sampleList_2016
from NanoAOD_Gen_Samples_2017 import sampleList_2017
from NanoAOD_Gen_Samples_2018 import sampleList_2018

newSamples = []
directory = '/store/user/rverma/Output/cms-hcs-run2/Skim-NanoAOD/'
for year in [2016,2017,2018]:
    skimFiles = open('Skim_NanoAOD_Files_%i.sh'%year,'w')
    sampleList = eval("sampleList_%i"%year)
    fileList = subprocess.Popen('xrdfs root://cmseos.fnal.gov/ ls %s%i'%(directory, year),shell=True,stdout=subprocess.PIPE).communicate()[0].split('\n')
    newSamples = []
    #print fileList
    for x in fileList:
        if len(x)>1:
            sample = x.split('/')[-1]
            sType = sample.split('_%i_skim'%year)[0]
            if 'ext' in sample:
                sType = sample.split('_ext')[0]
            if not sType in newSamples:
                newSamples.append(sType)

    newSamples.sort()
    samples = newSamples[:]
    unUsed = fileList[:]
    
    #print(unUsed)
    for s in samples:
        line = '%s_FileList_%i="'%(s, year)
        hasAny=False
        sType = '%s%i/%s_%i'%(directory, year, s,year)
        sType_ext = '%s%i/%s_ext'%(directory, year, s)
        for f in fileList:
            if f.startswith(sType) or f.startswith(sType_ext):
                #print(s,f)
                # if '%s_Pt'%s in f: continue
                # if '%s_Tune'%s in f: continue
                # if '%s_erd'%s in f: continue
                hasAny=True
                unUsed.remove(f)
                line += 'root://cmseos.fnal.gov/%s '%(f)
        line = line[:-1] + '"\n'
        if hasAny:
            print(line)
            skimFiles.write(line)
    skimFiles.close()
