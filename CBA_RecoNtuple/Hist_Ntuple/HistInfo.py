btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]
def GetHistogramInfo(extraCuts="(passPresel_Mu && nJet>=4 && nBJet>=2)*", nBJets=1):

    histogramInfo = { "presel_jet1Pt"                         : ["jetPt[0]"  , "presel_jet1Pt"   ,    [1000,0,1000], extraCuts      , "", True],
                      "presel_fwdjet1Pt"                      : ["fwdJetPt[0]","presel_fwdjet1Pt"   , [1000,0,1000], extraCuts      , "", True],
                      "presel_jet2Pt"                         : ["jetPt[1]"  , "presel_jet2Pt"   ,      [600,0,600], extraCuts      , "", True],
                      "presel_jet3Pt"                         : ["jetPt[2]"  , "presel_jet3Pt"   ,      [600,0,600], extraCuts      , "", True],
                      "presel_jet4Pt"                         : ["jetPt[3]"  , "presel_jet4Pt"   ,      [600,0,600], extraCuts      , "", True],
                      "presel_Njet"                           : ["nJet"      , "presel_Njet"     ,        [16,-0.5,15.5], extraCuts      , "", True],
                      "presel_NFwdjet"                        : ["nfwdJet"   , "presel_NFwdjet"     ,        [15,0,15], extraCuts      , "", True],
                      "presel_Nbjet"                          : ["nBJet"     , "presel_Nbjet"    ,        [10,0,10], extraCuts      , "", True],
                      "presel_muPt"                           : ["muPt"      , "presel_muPt"     ,      [600,0,600], extraCuts      , "", True],
                      "presel_muEta"                          : ["muEta"     , "presel_muEta"    ,   [100,-2.4,2.4], extraCuts      , "", True],
                      "presel_muPhi"                          : ["muPhi"     , "presel_muPhi"    , [100,-3.15,3.15], extraCuts      , "", True],
                      "presel_elePt"                          : ["elePt"     , "presel_elePt"    ,      [600,0,600], extraCuts      , "", True],
                      "presel_eleSCEta"                       : ["eleSCEta"  , "presel_eleSCEta" ,   [100,-2.4,2.4], extraCuts      , "", True],
                      "presel_elePhi"                         : ["elePhi"    , "presel_elePhi"   , [100,-3.15,3.15], extraCuts      , "", True],
                      "presel_M3"                             : ["M3"        , "presel_M3"       ,     [550,50,600], extraCuts      , "", True],
                      "presel_MET"                            : ["pfMET"     , "presel_MET"      ,      [300,0,600], extraCuts      , "", True],
   #                   "presel_METPhi"                         : ["pfMETPhi"  , "presel_METPhi"   , [100,-3.15,3.15], extraCuts      , "", True],
                      "presel_nVtx"                           : ["nVtx"      , "presel_nVtx"     ,        [50,0,50], extraCuts      , "", True],
                      "presel_WtransMass"                     : ["WtransMass","presel_WtransMass",      [200,0,200], extraCuts      , "", True],
                      "presel_HT"                             : ["HT"        ,"presel_HT"        ,   [1500,0,1500], extraCuts      , "", True],
                      "presel_nVtxup"                         : ["nVtx"      , "presel_nVtxup"   ,        [50,0,50], extraCuts      , "%sevtWeight*PUweight_Up*muEffWeight*eleEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets]), False],
                      "presel_nVtxdo"                         : ["nVtx"      , "presel_nVtxdo"   ,        [50,0,50], extraCuts      , "%sevtWeight*PUweight_Do*muEffWeight*eleEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets]), False],
                      "presel_nVtxNoPU"                       : ["nVtx"      , "presel_nVtxNoPU" ,        [50,0,50], extraCuts      , "%sevtWeight*muEffWeight*eleEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets]), False]
                      }
    return histogramInfo

allPlotList = ["presel_Njet","presel_elePt","presel_eleSCEta","presel_muEta","presel_jet1Pt","presel_nVtx","presel_nVtxdo","presel_nVtxup","presel_HT", "presel_M3"]
