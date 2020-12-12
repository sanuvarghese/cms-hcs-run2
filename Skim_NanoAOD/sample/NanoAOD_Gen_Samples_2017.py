#MCType = 'RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1'
MCType = 'RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1'
MCType_pmx = MCType.replace('102X','new_pmx_102X')
MCType_v2 = MCType.replace('-v1','-v2')
MCType_ext1 = MCType.replace('-v1','_ext1-v1')
MCType_ext2 = MCType.replace('-v1','_ext2-v1')
MCType_RECOSIM = MCType.replace('PU2017','PU2017RECOSIMstep')
MCType_RECOSIM_ext1 = MCType_RECOSIM.replace('-v1','_ext1-v1')
MCType_oddTTZ = 'RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_v7_102X_mc2017_realistic_v7-v1'
                 
MCType_oddWW = 'RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1'

DataType='Nano1June2019-v1'

MCType16='RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1'
sampleList_2017 = {
'HplusM080' : '/ChargedHiggsToCS_M080_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
'HplusM090' : '/ChargedHiggsToCS_M090_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
'HplusM100' : '/ChargedHiggsToCS_M100_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
'HplusM120' : '/ChargedHiggsToCS_M120_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
'HplusM140' : '/ChargedHiggsToCS_M140_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
'HplusM150' : '/ChargedHiggsToCS_M150_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
'HplusM155' : '/ChargedHiggsToCS_M155_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
'HplusM160' : '/ChargedHiggsToCS_M160_13TeV-madgraph/'+MCType16+'/NANOAODSIM',

'Data_SingleMu_b' : '/SingleMuon/Run2017B-'+DataType+'/NANOAOD',
'Data_SingleMu_c' : '/SingleMuon/Run2017C-'+DataType+'/NANOAOD',
'Data_SingleMu_d' : '/SingleMuon/Run2017D-'+DataType+'/NANOAOD',
'Data_SingleMu_e' : '/SingleMuon/Run2017E-'+DataType+'/NANOAOD',
'Data_SingleMu_f' : '/SingleMuon/Run2017F-'+DataType+'/NANOAOD',

'Data_SingleEle_b' : '/SingleElectron/Run2017B-'+DataType+'/NANOAOD',
'Data_SingleEle_c' : '/SingleElectron/Run2017C-'+DataType+'/NANOAOD',
'Data_SingleEle_d' : '/SingleElectron/Run2017D-'+DataType+'/NANOAOD',
'Data_SingleEle_e' : '/SingleElectron/Run2017E-'+DataType+'/NANOAOD',
'Data_SingleEle_f' : '/SingleElectron/Run2017F-'+DataType+'/NANOAOD',


'TTbarPowheg_Dilepton' : '/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType_pmx+'/NANOAODSIM',
'TTbarPowheg_Hadronic' : '/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType_pmx+'/NANOAODSIM',
'TTbarPowheg_Semilept' : '/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType+'/NANOAODSIM',


'W1jets'      : '/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType+'/NANOAODSIM',
'W2jets'      : '/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType+'/NANOAODSIM',
'W3jets'      : '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType_v2+'/NANOAODSIM',
'W4jets'      : '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType_pmx+'/NANOAODSIM',

'DYjetsM10to50'      : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType_v2+'/NANOAODSIM',
'DYjetsM10to50_ext1' : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType_ext1+'/NANOAODSIM',

'DYjetsM50_ext1' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType_RECOSIM+'/NANOAODSIM',
'DYjetsM50_ext2' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType_RECOSIM_ext1+'/NANOAODSIM',



'ST_s_channel'     : '/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/'+MCType_pmx+'/NANOAODSIM',
'ST_t_channel'     : '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType+'/NANOAODSIM',
'ST_tbar_channel'  : '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType+'/NANOAODSIM',
'ST_tW_channel'    : '/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType_pmx+'/NANOAODSIM',
'ST_tbarW_channel' : '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType+'/NANOAODSIM',



'TTWtoQQ'       : '/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/'+MCType+'/NANOAODSIM',
'TTWtoLNu' : '/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/'+MCType_oddWW+'/NANOAODSIM',
'TTZtoLL'  : '/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/'+MCType+'/NANOAODSIM',
'TTZtoLL_M1to10' : '/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType_oddTTZ+'/NANOAODSIM',
'TTZtoQQ'        : '/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType+'/NANOAODSIM',
'TTZtoQQ_ext1'   : '/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType_ext1+'/NANOAODSIM',


'WW'      : '/WW_TuneCP5_13TeV-pythia8/'+MCType+'/NANOAODSIM',
'WZ'      : '/WZ_TuneCP5_13TeV-pythia8/'+MCType+'/NANOAODSIM',
'ZZ'      : '/ZZ_TuneCP5_13TeV-pythia8/'+MCType_v2+'/NANOAODSIM',

'WWTo1L1Nu2Q_amcatnlo' : '/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType_oddWW+'/NANOAODSIM',
'WWToLNuQQ_powheg' : '/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType_ext1+'/NANOAODSIM',
'WWTo2L2Nu_powheg' : '/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType_ext1+'/NANOAODSIM',
'WWTo4Q_powheg' : '/WWTo4Q_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/'+MCType_ext1+'/NANOAODSIM',

'WZTo1L3Nu_amcatnlo' : '/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/'+MCType+'/NANOAODSIM',
'WZTo1L1Nu2Q_amcatnlo' : '/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType+'/NANOAODSIM',
'WZTo2L2Q_amcatnlo' : '/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType+'/NANOAODSIM',
'WZTo3LNu_powheg' : '/WZTo3LNu_13TeV-powheg-pythia8/'+MCType+'/NANOAODSIM',

'ZZTo2L2Q_amcatnlo' : '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType+'/NANOAODSIM',
'ZZTo2L2Nu_powheg' : '/ZZTo2L2Nu_13TeV_powheg_pythia8/'+MCType+'/NANOAODSIM',
'ZZTo2Q2Nu_amcatnlo' : '/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType+'/NANOAODSIM',
'ZZTo4L_powheg' : '/ZZTo4L_13TeV_powheg_pythia8/'+MCType+'/NANOAODSIM',
'ZZTo4L_powheg_ext1' : '/ZZTo4L_13TeV_powheg_pythia8/'+MCType_ext1+'/NANOAODSIM',
'ZZTo4L_powheg_ext2' : '/ZZTo4L_13TeV_powheg_pythia8/'+MCType_ext2+'/NANOAODSIM',

'VVTo2L2Nu_amcatnlo' : '/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/'+MCType+'/NANOAODSIM',

'QCD_Pt20to30_Mu'         : '/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt30to50_Mu'         : '/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt50to80_Mu'         : '/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt80to120_Mu'        : '/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt120to170_Mu'       : '/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt170to300_Mu'       : '/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt300to470_Mu'       : '/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt470to600_Mu'       : '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt600to800_Mu'       : '/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt800to1000_Mu'      : '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt1000toInf_Mu'      : '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',

'QCD_Pt20to30_Ele'        : '/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt30to50_Ele'        : '/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt50to80_Ele'        : '/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt80to120_Ele'       : '/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt120to170_Ele'      : '/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt170to300_Ele'      : '/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',
'QCD_Pt300toInf_Ele'      : '/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType+'/NANOAODSIM',

}
