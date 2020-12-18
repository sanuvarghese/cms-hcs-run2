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

#-----------------------------------------
#Name of the ROOT files
#----------------------------------------
samples = {"HplusM080" : [HplusM080],
           "HplusM090" : [HplusM090],  
           "HplusM100" : [HplusM100],  
           "HplusM120" : [HplusM120],  
           "HplusM140" : [HplusM140],  
           "HplusM150" : [HplusM150],  
           "HplusM155" : [HplusM155],  
           "HplusM160" : [HplusM160],  

           "TTbar" : [TTbarPowheg_Hadronic + 
               TTbarPowheg_Dilepton + 
               TTbarPowheg_Semilept],  
           "Wjets" : [W1jets + 
               W2jets + 
               W3jets + 
               W4jets],  
           "ZJets" : [DYjetsM50_ext1+ 
               DYjetsM10to50],  
           "SingleTop" : [ST_tbarW_channel + 
               ST_s_channel + 
               ST_t_channel + 
               ST_tbar_channel + 
               ST_tW_channel],  
           "TTV" : [TTWtoQQ + 
               TTZtoQQ + 
               TTWtoLNu_ext1+
               TTWtoLNu_ext2 + 
               TTZtoLL_M1to10+ 
               TTZtoLL_ext3+ 
               TTZtoLL_ext2+ 
               TTZtoLL_ext1],  
           "QCDEle"   : [QCD_Pt20to30_Ele +
                           QCD_Pt30to50_Ele+
                           QCD_Pt50to80_Ele+
                           QCD_Pt80to120_Ele+
                           QCD_Pt120to170_Ele+
                           QCD_Pt170to300_Ele+
                           QCD_Pt300toInf_Ele],
           "QCDMu"    : [QCD_Pt20to30_Mu+
                          QCD_Pt30to50_Mu+
                          QCD_Pt50to80_Mu+
                          QCD_Pt80to120_Mu+
                          QCD_Pt120to170_Mu+
                          QCD_Pt170to300_Mu+
                          QCD_Pt300to470_Mu+
                          QCD_Pt470to600_Mu+
                          QCD_Pt600to800_Mu+
                          QCD_Pt800to1000_Mu+
                          QCD_Pt1000toInf_Mu
                         ],
           "Diboson" : [WW + WZ + ZZ],  

           "DataEle" : [Data_SingleEle_b + 
               Data_SingleEle_c + 
               Data_SingleEle_d + 
               Data_SingleEle_e + 
               Data_SingleEle_f + 
               Data_SingleEle_g + 
               Data_SingleEle_h],  
           "DataMu" : [Data_SingleMu_b + 
               Data_SingleMu_c + 
               Data_SingleMu_d + 
               Data_SingleMu_e + 
               Data_SingleMu_f + 
               Data_SingleMu_g + 
               Data_SingleMu_h] 
          }
