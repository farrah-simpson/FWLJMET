import os, sys, argparse, imp
import datetime
cTime=datetime.datetime.now()
date_str='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)

userName = os.environ['USER']
relBase = os.environ['CMSSW_BASE']
home = os.environ['HOME']

parser = argparse.ArgumentParser()
parser.add_argument("-f","--finalState",action="store")
parser.add_argument("-y","--year",action="store")
parser.add_argument("--shifts",action="store_true")
parser.add_argument("--brux",action="store_true")
parser.add_argument("-o","--outfolder",action="store",default="default")
option = parser.parse_args()

if option.finalState not in [ "singleLep", "doubleLep", "multiLep" ]: quit( "[ERR] Invalid -f (--finalState) argument passed." )
if option.year not in [ "2016APV", "2016", "2017", "2018" ]: quit( "[ERR] Invalid -y (--year) argument passed." )
SHIFTS = "True" if option.shifts else "False"
	
#Sample list file
sampleListPath = "sample_list_"+option.finalState+option.year+"UL.py"
sample = imp.load_source("Sample",sampleListPath,open(sampleListPath,"r"))

####################
### SET YOUR STRINGS
####################
#cmsRun config

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

def create_crab_config_files_from_template(sample_dict,**kwargs):

	for dataset in sample_dict:

		print dataset,sample_dict[dataset]

		filename = 'crab_config_shifts_{}.py'.format( dataset ) if kwargs["SHIFTS"] else "crab_config_{}.py".format( dataset )
		cmsRunname = 'runFWLJMet_shifts_{}.py'.format( dataset ) if kwargs["SHIFTS"] else "runFWLJMet_{}.py".format( dataset )

		#copy template file to new directory
		os.system('cp -v '+CRABCONFIG_TEMPLATE+' '+CRABCONFIG_DIR+'/'+filename)
		os.system('cp -v '+CMSRUNCONFIG+' '+CRABCONFIG_DIR+'/'+cmsRunname)

		#replace strings in new crab file
		os.system("sed -i 's|CMSRUNCONFIG|"+CRABCONFIG_DIR+"/"+cmsRunname+"|g' "+CRABCONFIG_DIR+"/"+filename)
		os.system("sed -i 's|INPUT|"+sample_dict[dataset]+"|g' "+CRABCONFIG_DIR+"/"+filename)
		os.system("sed -i 's|REQNAME|"+REQNAME+"|g' "+CRABCONFIG_DIR+"/"+filename)
		os.system("sed -i 's|OUTFOLDER|"+OUTFOLDER+"|g' "+CRABCONFIG_DIR+"/"+filename)
		os.system("sed -i 's|LOGFOLDER|"+dataset+"|g' "+CRABCONFIG_DIR+"/"+filename)
		os.system("sed -i 's|JSONFORDATA|"+JSONDATA[option.year]+"|g' "+CRABCONFIG_DIR+"/"+filename)
		os.system("sed -i 's|ISMC|"+kwargs['ISMC']+"|g' "+CRABCONFIG_DIR+"/"+filename)
		os.system("sed -i 's|ISVLQSIGNAL|"+kwargs['ISVLQSIGNAL']+"|g' "+CRABCONFIG_DIR+"/"+filename)
                os.system("sed -i 's|CRABSUBMITLOG|"+CRABSUBMIT_DIR+"|g' "+CRABCONFIG_DIR+"/"+filename)

		#replace strings in new cmsRun file
		if 'EGamma' in dataset or 'Single' in dataset or 'JetHT' in dataset:
			os.system("sed -i 's|DATASET|"+dataset+"|g' "+CRABCONFIG_DIR+"/"+cmsRunname)
		elif 'ext' in dataset:
			extcode = dataset[dataset.find('ext'):]
			os.system("sed -i 's|DATASET|"+sample_dict[dataset].split('/')[1]+'-'+extcode+"|g' "+CRABCONFIG_DIR+"/"+cmsRunname)
		else:
			os.system("sed -i 's|DATASET|"+sample_dict[dataset].split('/')[1]+"|g' "+CRABCONFIG_DIR+"/"+cmsRunname)
		os.system("sed -i 's|ISMC|"+kwargs['ISMC']+"|g' "+CRABCONFIG_DIR+"/"+cmsRunname)
		os.system("sed -i 's|ISVLQSIGNAL|"+kwargs['ISVLQSIGNAL']+"|g' "+CRABCONFIG_DIR+"/"+cmsRunname)		
		os.system("sed -i 's|ISTTBAR|"+kwargs['ISTTBAR']+"|g' "+CRABCONFIG_DIR+"/"+cmsRunname)
		os.system("sed -i 's|DOGENHT|"+kwargs['DOGENHT']+"|g' "+CRABCONFIG_DIR+"/"+cmsRunname)
		os.system("sed -i 's|SHIFTS|" + kwargs["SHIFTS"] + "|g' " + CRABCONFIG_DIR + "/" + cmsRunname)

		os.system("sed -i 's|OUTPATH|"+OUTPATH+"|g' "+CRABCONFIG_DIR+"/"+filename)
		os.system("sed -i 's|STORESITE|"+STORESITE+"|g' "+CRABCONFIG_DIR+"/"+filename)


if __name__=='__main__':

	os.system('mkdir -vp '+CRABCONFIG_DIR)

	#### Bkg MC - no ttbar - yes MLM
	create_crab_config_files_from_template(
		sample.bkghtdict,
		ISMC='True',
		ISVLQSIGNAL='False',
		ISTTBAR='False',
 		DOGENHT='True',
		SHIFTS=SHIFTS
		)

	#### Bkg MC - no ttbar - no MLM
	create_crab_config_files_from_template(
		sample.bkgdict,
		ISMC='True',
		ISVLQSIGNAL='False',
		ISTTBAR='False',
 		DOGENHT='False',
		SHIFTS=SHIFTS
		)

	#### Bkg MC - ttbar
	create_crab_config_files_from_template(
 		sample.ttbarbkgdict,
 		ISMC='True',
 		ISVLQSIGNAL='False',
 		ISTTBAR='True',
 		DOGENHT='False',
		SHIFTS=SHIFTS
 		)

        #### fourtops MC
        create_crab_config_files_from_template(
                sample.fourtopssigdict,
                ISMC='True',
                ISVLQSIGNAL='False',
                ISTTBAR='False',
 		DOGENHT='False',
		SHIFTS=SHIFTS
                )
        create_crab_config_files_from_template(
                sample.fourtopsttdict,
                ISMC='True',
                ISVLQSIGNAL='False',
                ISTTBAR='True',
 		DOGENHT='False',
		SHIFTS=SHIFTS
                )
        create_crab_config_files_from_template(
                sample.fourtopsbkgdict,
                ISMC='True',
                ISVLQSIGNAL='False',
                ISTTBAR='False',
 		DOGENHT='False',
		SHIFTS=SHIFTS
                )

	#### VLQ signal MC
	create_crab_config_files_from_template(
		sample.signaldict,
		ISMC='True',
		ISVLQSIGNAL='True',
		ISTTBAR='False',
		DOGENHT='False',
		SHIFTS=SHIFTS
		)

	#### Data
	create_crab_config_files_from_template(
	 	sample.datadict,
	 	ISMC='False',
	 	ISVLQSIGNAL='False',
	 	ISTTBAR='False',
	 	DOGENHT='False',
		SHIFTS="False"
	 	)
