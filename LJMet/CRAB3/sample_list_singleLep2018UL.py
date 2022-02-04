import os,sys

signaldict = {}

##VLQ TT -- no UL production
#signaldict['TpTp1800'] = '/TprimeTprime_M-1800_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['TpTp1700'] = '/TprimeTprime_M-1700_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['TpTp1600'] = '/TprimeTprime_M-1600_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['TpTp1500'] = '/TprimeTprime_M-1500_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
#signaldict['TpTp1400'] = '/TprimeTprime_M-1400_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['TpTp1300'] = '/TprimeTprime_M-1300_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['TpTp1200'] = '/TprimeTprime_M-1200_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['TpTp1100'] = '/TprimeTprime_M-1100_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['TpTp1000'] = '/TprimeTprime_M-1000_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['TpTp900'] = '/TprimeTprime_M-900_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'

##VLQ BB
#signaldict['BpBp1800'] = '/BprimeBprime_M-1800_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['BpBp1700'] = '/BprimeBprime_M-1700_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['BpBp1600'] = '/BprimeBprime_M-1600_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM'
#signaldict['BpBp1500'] = '/BprimeBprime_M-1500_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['BpBp1400'] = '/BprimeBprime_M-1400_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['BpBp1300'] = '/BprimeBprime_M-1300_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['BpBp1200'] = '/BprimeBprime_M-1200_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['BpBp1100'] = '/BprimeBprime_M-1100_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['BpBp1000'] = '/BprimeBprime_M-1000_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
#signaldict['BpBp900'] = '/BprimeBprime_M-900_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'

signaldict['Hptb200'] = '/ChargedHiggs_HplusTB_HplusToTB_M-200_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb220'] = '/ChargedHiggs_HplusTB_HplusToTB_M-220_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb250'] = '/ChargedHiggs_HplusTB_HplusToTB_M-250_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb300'] = '/ChargedHiggs_HplusTB_HplusToTB_M-300_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb350'] = '/ChargedHiggs_HplusTB_HplusToTB_M-350_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb400'] = '/ChargedHiggs_HplusTB_HplusToTB_M-400_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb500'] = '/ChargedHiggs_HplusTB_HplusToTB_M-500_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb600'] = '/ChargedHiggs_HplusTB_HplusToTB_M-600_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb700'] = '/ChargedHiggs_HplusTB_HplusToTB_M-700_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb800'] = '/ChargedHiggs_HplusTB_HplusToTB_M-800_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb1000'] = '/ChargedHiggs_HplusTB_HplusToTB_M-1000_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb1250'] = '/ChargedHiggs_HplusTB_HplusToTB_M-1250_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb1500'] = '/ChargedHiggs_HplusTB_HplusToTB_M-1500_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb1750'] = '/ChargedHiggs_HplusTB_HplusToTB_M-1750_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb2000'] = '/ChargedHiggs_HplusTB_HplusToTB_M-2000_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb2500'] = '/ChargedHiggs_HplusTB_HplusToTB_M-2500_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
signaldict['Hptb3000'] = '/ChargedHiggs_HplusTB_HplusToTB_M-3000_TuneCP5_13TeV_amcatnlo_pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'

bkgdict = {}
bkghtdict = {}

#DYJetsToLL M-50
bkghtdict['DYM50HT200to400'] = '/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
bkghtdict['DYM50HT400to600'] = '/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v3/MINIAODSIM'
bkghtdict['DYM50HT600to800'] = '/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
bkghtdict['DYM50HT800to1200'] = '/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
bkghtdict['DYM50HT1200to2500'] = '/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
bkghtdict['DYM50HT2500toInf'] = '/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'

#WJetsToLNu
#bkgdict['WJets'] = '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM' (inclusive)
#bkghtdict['WJetsHT70to100'] = '/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM' (below acceptance)
#bkghtdict['WJetsHT100to200'] = '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM' (below acceptance)
bkghtdict['WJetsHT200to400'] = '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['WJetsHT400to600'] = '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['WJetsHT600to800'] = '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['WJetsHT800to1200'] = '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['WJetsHT1200to2500'] = '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['WJetsHT2500toInf'] = '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'

#TTWJets
bkgdict['TTW'] = '/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
#TTZ
bkgdict['TTZM10'] = '/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
bkgdict['TTZM1to10'] = '/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
#TTH
bkgdict['TTHbb'] = '/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM'
bkgdict['TTHnonbb'] = '/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'


# <<< SM single top bck >>>
#tW
bkgdict['ST_tW_antitop'] = '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM'
bkgdict['ST_tW_top'] = '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM'
bkgdict['ST_t_antitop'] = '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkgdict['ST_t_top'] = '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkgdict['ST_s'] = '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM'

# <<< diboson >>>
bkgdict['WW'] = '/WW_TuneCP5_PSweights_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkgdict['WZ'] = '/WZ_TuneCP5_PSweights_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkgdict['ZZ'] = '/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'

# <<< QCD >>>
bkghtdict['QCD200'] = '/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['QCD300'] = '/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['QCD500'] = '/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['QCD700'] = '/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['QCD1000'] = '/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['QCD1500'] = '/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
bkghtdict['QCD2000'] = '/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'

ttbarbkgdict = {}

# <<< SM ttbar bck >>>
#(only TT_Mtt-700to1000 is available for Autumn2018, so use inclusive samples) - 20 May, 2019
ttbarbkgdict['TTToHadronic'] = '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
ttbarbkgdict['TTToSemiLeptonic'] = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
ttbarbkgdict['TTTo2L2Nu'] = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
ttbarbkgdict['TTToSemiLepton_HT500Njet9'] = '/TTToSemiLepton_HT500Njet9_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
ttbarbkgdict['TT_Mtt700'] = '/TT_Mtt-700to1000_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
ttbarbkgdict['TT_Mtt1000'] = '/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'

datadict = {}

datadict['SingleElectronRun2018A']  = '/EGamma/Run2018A-17Sep2018-v2/MINIAOD'
datadict['SingleElectronRun2018B']  = '/EGamma/Run2018B-17Sep2018-v1/MINIAOD'
datadict['SingleElectronRun2018C']  = '/EGamma/Run2018C-17Sep2018-v1/MINIAOD'
datadict['SingleElectronRun2018D']  = '/EGamma/Run2018D-PromptReco-v2/MINIAOD'

datadict['SingleMuonRun2018A']  = '/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD'
datadict['SingleMuonRun2018B']  = '/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD'
datadict['SingleMuonRun2018C']  = '/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD'
datadict['SingleMuonRun2018D']  = '/SingleMuon/Run2018D-PromptReco-v2/MINIAOD'

datadict['JetHTRun2018A'] = '/JetHT/Run2018A-17Sep2018-v1/MINIAOD'
datadict['JetHTRun2018B'] = '/JetHT/Run2018B-17Sep2018-v1/MINIAOD'
datadict['JetHTRun2018C'] = '/JetHT/Run2018C-17Sep2018-v1/MINIAOD'
datadict['JetHTRun2018D'] = '/JetHT/Run2018D-PromptReco-v2/MINIAOD'

fourtopssigdict = {}
fourtopsttdict = {}
fourtopsbkgdict = {}

fourtopssigdict['TTTT'] = '/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'

fourtopsttdict['TTToSemiLeptonic_TuneCP5down'] = '/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
fourtopsttdict['TTToSemiLeptonic_TuneCP5up'] = '/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
fourtopsttdict['TTToHadronic_TuneCP5down'] = '/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
fourtopsttdict['TTToHadronic_TuneCP5up'] = '/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
fourtopsttdict['TTTo2L2Nu_TuneCP5down'] = '/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
fourtopsttdict['TTTo2L2Nu_TuneCP5up'] = '/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
fourtopsttdict['TTToSemiLeptonic_hdampUP'] ='/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
fourtopsttdict['TTToSemiLeptonic_hdampDOWN'] ='/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
fourtopsttdict['TTWH'] = '/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
fourtopsttdict['TTWW'] = '/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
fourtopsttdict['TTWZ'] = '/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
fourtopsttdict['TTZZ'] = '/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
fourtopsttdict['TTZH'] = '/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
fourtopsttdict['TTHH'] = '/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
fourtopsttdict['TTTW'] = '/TTTW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
fourtopsttdict['TTTJ'] = '/TTTJ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
