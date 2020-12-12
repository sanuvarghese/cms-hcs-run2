from NanoAOD_Gen_Samples_2016 import sampleList_2016
from NanoAOD_Gen_Samples_2017 import sampleList_2017
from NanoAOD_Gen_Samples_2018 import sampleList_2018

from getFilesFromDisk import getFileList_DAS, getFileList_EOS

for year in [2016,2017,2018]:
    line = ""
    sampleList = eval("sampleList_%i"%year)
    for sampleName, sample in sampleList.items():
        print(sampleName)
        line += '%s_FileList_%i="'%(sampleName,year)
        if '/store/user/' in sample:
            line += getFileList_EOS(sample)
            line += '"\n\n'
        else:
            line += "xrootd "
            line += getFileList_DAS(sample)
            line += '"\n\n'
    with open('NanoAOD_Gen_Files_%i.sh'%year,'wb') as _file:
        _file.write(line.encode('ascii'))
