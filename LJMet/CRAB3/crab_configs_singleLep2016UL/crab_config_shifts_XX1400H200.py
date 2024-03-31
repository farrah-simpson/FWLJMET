from WMCore.Configuration import Configuration
config = Configuration()

import datetime,os
cTime=datetime.datetime.now()
date_str='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)

relBase = os.environ['CMSSW_BASE']
home = os.environ['HOME']

####################
### SET YOUR STRINGS
####################
cmsRun_config  = 'crab_configs_singleLep2016UL/runFWLJMet_shifts_XX1400H200.py'
inputDataset   = '/PairVLQ_x53x53_tHtH_narrow_RH_MX1400_MH200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM'
requestName    = 'singleLep2016UL'
outputFolder   = 'FWLJMET106XUL_singleLep2016UL_RunIISummer20v2'
logFolder      = 'XX1400H200'
Json_for_data  = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt'
isMC           = True
isVLQsignal    = True
isTTbar        = False
##############
### GENERAL
##############
config.section_("General")
config.General.requestName = logFolder
config.General.workArea = "logs_" + requestName 
config.General.transferLogs = True
config.General.transferOutputs = True


##############
### JobType
##############
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = cmsRun_config

#for VLQ signal this will run using crab_script.sh which will reset the env var in order to access LHApdf outside of CMSSW
if isVLQsignal:
	config.JobType.scriptExe = relBase+'/src/FWLJMET/LJMet/CRAB3/crab_script.sh'
	
# runtime, memory, cores
if isMC:
	config.JobType.maxJobRuntimeMin = 2750 #minutes
config.JobType.maxMemoryMB = 4000 #MB, believed to be per core based on CRAB3FAQ TWiki, evidently not based on tests
config.JobType.numCores = 4 #use wisely if turned on.

##############
### DATA
##############
config.section_("Data")
config.Data.inputDataset = inputDataset
config.Data.allowNonValidInputDataset = True
if isMC:
	#config.Data.splitting = 'Automatic'
	#config.Data.unitsPerJob = 1440 # 24 hours
	if isVLQsignal:
		config.Data.splitting = 'LumiBased'
		config.Data.unitsPerJob = 2
	elif isTTbar:
                config.Data.splitting = "LumiBased"
                config.Data.unitsPerJob = 1
	else:
		config.Data.splitting = 'FileBased'
		config.Data.unitsPerJob = 1
else:
	config.Data.splitting = 'LumiBased'
	config.Data.unitsPerJob = 1
	config.Data.lumiMask = Json_for_data

config.Data.inputDBS = 'global'
config.Data.ignoreLocality = False
config.Data.publication = False
# This string is used to construct the output dataset name : /store/user/lpcljm/<outputFolder>/<inpuDataset>/<requestName>/<someCRABgeneratedNumber>/<someCRABgeneratedNumber>/
config.Data.outputDatasetTag = requestName
config.Data.outLFNDirBase = '/store/group/lpcljm/' + outputFolder

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
