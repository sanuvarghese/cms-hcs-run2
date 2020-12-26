
from RecoNtuple_Skim_FileLists_cff import *
#-----------------------------------------
#INPUT AnalysisNtuples Directory
#----------------------------------------
dirBase = "root://cmseos.fnal.gov//store/user/rverma/Output/cms-hcs-run2/RecoNtuple_Skim" 
dirBaseCR = dirBase
dirSyst = dirBase
dirSystCR = dirBase
dirBaseDilep = dirBase
dirSystDilep = dirBase

era16 = ["b", "c", "d", "e", "f", "g", "h"]
era17 = ["b", "c", "d", "e", "f"]
era18 = ["a", "b", "c", "d"]
data16Mu = []
data17Mu = []
data18Mu = []
data16Ele = []
data17Ele = []
data18Ele = []
for d in era16:
    data16Mu.append("Data_SingleMu_%s"%d)
    data16Ele.append("Data_SingleEle_%s"%d)
for d in era17:
    data17Mu.append("Data_SingleMu_%s"%d)
    data17Ele.append("Data_SingleEle_%s"%d)
for d in era18:
    data18Mu.append("Data_SingleMu_%s"%d)
    data18Ele.append("Data_SingleEle_%s"%d)
dataAllMu = {"2016":data16Mu, "2017":data17Mu, "2018":data18Mu}
dataAllEle = {"2016":data16Ele, "2017":data17Ele, "2018":data18Ele}
def gs(year, s_array):
    sample = []
    for s in s_array:
        sample += eval("%s_%s"%(s, year))
    return sample

def getSamples(y):
    samples = {"HplusM080" : gs(y, ["HplusM080"]),
               "HplusM090" : gs(y, ["HplusM090"]),  
               "HplusM100" : gs(y, ["HplusM100"]),  
               "HplusM120" : gs(y, ["HplusM120"]),  
               "HplusM140" : gs(y, ["HplusM140"]),  
               "HplusM150" : gs(y, ["HplusM150"]),  
               "HplusM155" : gs(y, ["HplusM155"]),  
               "HplusM160" : gs(y, ["HplusM160"]),  

               "TTbar" : gs(y, ["TTbarPowheg_Hadronic" , 
                   "TTbarPowheg_Dilepton" , 
                   "TTbarPowheg_Semilept"]),  
               "Wjets" : gs(y, ["W1jets" , 
                   "W2jets" , 
                   "W3jets" , 
                   "W4jets"]),  
               "ZJets" : gs(y, ["DYjetsM50", 
                   "DYjetsM10to50"]),  
               "SingleTop" : gs(y, ["ST_tbarW_channel" , 
                   "ST_s_channel" , 
                   "ST_t_channel" , 
                   "ST_tbar_channel" , 
                   "ST_tW_channel"]),  
               "TTV" : gs(y, ["TTWtoQQ" , 
                   "TTZtoQQ" , 
                   "TTWtoLNu",
                   "TTZtoLL_M1to10", 
                   "TTZtoLL"]),  
               "QCDEle"   : gs(y, ["QCD_Pt20to30_Ele",
                               "QCD_Pt30to50_Ele",
                               "QCD_Pt50to80_Ele",
                               "QCD_Pt80to120_Ele",
                               "QCD_Pt120to170_Ele",
                               "QCD_Pt170to300_Ele",
                               "QCD_Pt300toInf_Ele"]),
               "QCDMu"    : gs(y, ["QCD_Pt20to30_Mu",
                              "QCD_Pt30to50_Mu",
                              "QCD_Pt50to80_Mu",
                              "QCD_Pt80to120_Mu",
                              "QCD_Pt120to170_Mu",
                              "QCD_Pt170to300_Mu",
                              "QCD_Pt300to470_Mu",
                              "QCD_Pt470to600_Mu",
                              "QCD_Pt600to800_Mu",
                              "QCD_Pt800to1000_Mu",
                              "QCD_Pt1000toInf_Mu"
                             ]),
               "Diboson" : gs(y, ["WW" , "WZ" , "ZZ"]),  

               "DataEle" : gs(y, dataAllEle[y]), 
               "DataMu" : gs(y, dataAllMu[y])
              }
    return samples


#a = getSamples("2017")
#print a
#print a.keys()
