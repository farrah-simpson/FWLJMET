import os, sys, argparse, imp
import datetime
cTime=datetime.datetime.now()
date_str='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)

userName = os.environ['USER']
relBase = os.environ['CMSSW_BASE']
home = os.environ['HOME']

parser = argparse.ArgumentParser()
parser.add_argument("-f","--finalState",action="store",help="singleLep")
parser.add_argument("-y","--year",action="store",help="2016APV,2016,2017,2018")
parser.add_argument("-g","--groups",nargs="+",required=True,help="See sample_list_*UL.py")
parser.add_argument("--shifts",action="store_true",help="JER/JEC shifts")
parser.add_argument("--brux",action="store_true",help="Store CRAB output on BRUX")
parser.add_argument("-o","--outfolder",action="store",default="default")
option = parser.parse_args()

if option.finalState not in [ "singleLep", "doubleLep", "multiLep" ]: quit( "[ERR] Invalid -f (--finalState) argument passed." )
if option.year not in [ "2016APV", "2016", "2017", "2018" ]: quit( "[ERR] Invalid -y (--year) argument passed." )
SHIFTS = "True" if option.shifts else "False"
	
#Sample list file
sampleListPath = "sample_list_{}{}UL.py".format( option.finalState, option.year )
samples = imp.load_source( "Sample", sampleListPath, open( sampleListPath, "r" ) )

####################
### SET YOUR STRINGS
####################

CMSRUNCONFIG        = '../runFWLJMet_{}{}UL.py'.format( option.finalState, option.year )

#folder to save the created crab configs
CRABCONFIG_DIR      = 'crab_configs_{}{}UL'.format( option.finalState, option.year )

#folder to store submit logs
CRABSUBMIT_DIR      = "crab_submit_{}{}UL".format( option.finalState, option.year )

#the crab cfg template to copy from
CRABCONFIG_TEMPLATE = 'crab_config_template.py'

#crab request name
REQNAME             = option.finalState+option.year + "UL"

#eos out folder
OUTFOLDER           = "FWLJMET106XUL_{}{}UL_RunIISummer20".format( option.finalState, option.year ) if option.outfolder == "default" else option.outfolder

#JSON for Data
JSONDATA = {
  "2016": "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt", # UL URL
  #"16": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt", # UL lxplus
  "2016APV": "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt", # UL URL
  #"16APV": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt", # UL lxplus
  "2017": "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt", # UL URL
  #"17": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt", # UL lxplus
  "2018": "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt", # UL URL
  #"18": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt" # UL lxplus
}

if option.brux:
	OUTPATH = '/store/group/bruxljm/'
	STORESITE = 'T3_US_Brown'
else:
	OUTPATH = '/store/group/lpcljm/'
	STORESITE = 'T3_US_FNALLPC'

def create_crab_config( group, process, shifts ):
	ISMC = "True" if process not in samples.groups[ "DATA" ].keys() else "False"
	SHIFTS = "True" if shifts else "False"
	try: 
		ISVLQSIGNAL = "True" if process in samples.groups[ "VLQ" ].keys() else "False"
	except:
		ISVLQSIGNAL = "False"
	try: 
		ISTTBAR = "True" if ( ( process in samples.groups[ "TTBAR" ].keys() ) or ( process in samples.groups[ "TTMT" ].keys() ) or ( process in samples.groups[ "TTTX" ].keys() ) or ( process in samples.groups[ "TTBAR_SHIFTS" ].keys() ) or ( process in samples.groups[ "TTXY" ].keys() ) ) else "False"
	except:
		ISTTBAR = "False"
	try:
		DOGENHT = "True" if ( ( process in samples.groups[ "WJETSHT" ].keys() ) or ( process in samples.groups[ "QCDHT" ].keys() ) or ( process in samples.groups[ "DYMHT" ].keys() ) ) else "False"
	except:
		DOGENHT = "False"
		
	filename = 'crab_config_shifts_{}.py'.format( process ) if SHIFTS else "crab_config_{}.py".format( process )
	cmsRunname = 'runFWLJMet_shifts_{}.py'.format( process ) if SHIFTS else "runFWLJMet_{}.py".format( process )

	#copy template file to new directory
	os.system( 'cp -v {} {}/{}'.format( CRABCONFIG_TEMPLATE, CRABCONFIG_DIR, filename ) )
	os.system( 'cp -v {} {}/{}'.format( CMSRUNCONFIG, CRABCONFIG_DIR, cmsRunname ) )

	#replace strings in new crab file
	os.system( "sed -i 's|CMSRUNCONFIG|{}/{}|g' {}/{}".format( CRABCONFIG_DIR, cmsRunname, CRABCONFIG_DIR, filename ) )
	os.system( "sed -i 's|INPUT|{}|g' {}/{}".format( samples.groups[ group ][ process ], CRABCONFIG_DIR, filename ) )
	os.system( "sed -i 's|REQNAME|{}|g' {}/{}".format( REQNAME, CRABCONFIG_DIR, filename ) )
	os.system( "sed -i 's|OUTFOLDER|{}|g' {}/{}".format( OUTFOLDER, CRABCONFIG_DIR, filename ) )
	os.system( "sed -i 's|LOGFOLDER|{}|g' {}/{}".format( process, CRABCONFIG_DIR, filename ) )
	os.system( "sed -i 's|JSONFORDATA|{}|g' {}/{}".format( JSONDATA[option.year], CRABCONFIG_DIR, filename ) )
	os.system( "sed -i 's|ISMC|{}|g' {}/{}".format( ISMC, CRABCONFIG_DIR, filename ) )
	os.system( "sed -i 's|ISVLQSIGNAL|{}|g' {}/{}".format( ISVLQSIGNAL, CRABCONFIG_DIR, filename ) )
	os.system( "sed -i 's|CRABSUBMITLOG|{}|g' {}/{}".format( CRABSUBMIT_DIR, CRABCONFIG_DIR, filename ) )

	#replace strings in new cmsRun file
	if ( ( "EGamma" in process ) or ( "Single" in process ) or ( "JetHT" in process ) ):
		os.system( "sed -i 's|DATASET|{}|g' {}/{}".format( process, CRABCONFIG_DIR, cmsRunname ) )
	elif 'ext' in process:
		extcode = process[ process.find("ext"): ]
		os.system( "sed -i 's|DATASET|{}-{}|g' {}/{}".format( samples.groups[ group ][ process ].split("/")[1], extcode, CRABCONFIG_DIR, cmsRunname ) )
	else:
		os.system( "sed -i 's|DATASET|{}|g' {}/{}".format( samples.groups[ group ][ process ].split("/")[1], CRABCONFIG_DIR, cmsRunname ) )
	os.system( "sed -i 's|ISMC|{}|g' {}/{}".format( ISMC, CRABCONFIG_DIR, cmsRunname ) )
	os.system( "sed -i 's|ISVLQSIGNAL|{}|g' {}/{}".format( ISVLQSIGNAL, CRABCONFIG_DIR, cmsRunname ) )		
	os.system( "sed -i 's|ISTTBAR|{}|g' {}/{}".format( ISTTBAR, CRABCONFIG_DIR, cmsRunname ) )
	os.system( "sed -i 's|DOGENHT|{}|g' {}/{}".format( DOGENHT, CRABCONFIG_DIR, cmsRunname ) )
	os.system( "sed -i 's|SHIFTS|{}|g' {}/{}".format( SHIFTS, CRABCONFIG_DIR, cmsRunname ) )
	os.system( "sed -i 's|OUTPATH|{}|g' {}/{}".format( OUTPATH, CRABCONFIG_DIR, filename ) )
	os.system( "sed -i 's|STORESITE|{}|g' {}/{}".format( STORESITE, CRABCONFIG_DIR, filename ) )

if __name__=='__main__':
	
	os.system('mkdir -vp '+CRABCONFIG_DIR)

	for group in option.groups:
		if group not in list( samples.groups.keys() ):
			print( "[WARN] {} is not a valid group listed in 'sample_list_{}{}UL.py'. Skipping.".format( group, option.finalState, option.year ) )
		else:
			for process in samples.groups[ group ]:
				create_crab_config( group, process, SHIFTS )
