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
cmsRun_config  = 'CMSRUNCONFIG'
inputDataset   = 'INPUT'
requestName    = 'REQNAME'
outputFolder   = 'OUTFOLDER'
logFolder      = 'LOGFOLDER'
Json_for_data  = 'JSONFORDATA'
isMC           = ISMC
isVLQsignal    = ISVLQSIGNAL

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
	else:
		config.Data.splitting = 'FileBased'
		config.Data.unitsPerJob = 1
else:
	config.Data.splitting = 'Automatic'
	config.Data.unitsPerJob = 720 
	config.Data.lumiMask = Json_for_data

config.Data.inputDBS = 'global'
config.Data.ignoreLocality = False
config.Data.publication = False
# This string is used to construct the output dataset name : /store/user/lpcljm/<outputFolder>/<inpuDataset>/<requestName>/<someCRABgeneratedNumber>/<someCRABgeneratedNumber>/
config.Data.outputDatasetTag = requestName
config.Data.outLFNDirBase = 'OUTPATH' + outputFolder

config.section_("Site")
config.Site.storageSite = 'STORESITE'
