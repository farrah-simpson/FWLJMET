import os, argparse, imp

parser = argparse.ArgumentParser()
parser.add_argument("--finalState",action="store")
parser.add_argument("--year",action="store")
parser.add_argument("--test",action="store_true")
option = parser.parse_args()

#Sample list file
sampleListPath = "sample_list_"+option.finalState+option.year+"UL.py"
sample = imp.load_source("Sample",sampleListPath,open(sampleListPath,"r"))

home = os.environ['HOME']
CRABCONFIG_DIR      = 'crabConfigs_'+option.finalState+option.year+"UL"
#CRABCONFIG_DIR      = home+'/nobackup/FWLJMET102X_crabConfigs_'+option.finalState+option.year #JH: crab stuff in nobackup

def submit_multiple_crab_jobs(sample_dict):

	for dataset in sample_dict:

		print 'Submitting ',dataset,':',sample_dict[dataset]

		crab_cfg = CRABCONFIG_DIR+'/crab_FWLJMET_cfg_'+dataset+'.py'

		#os.system('echo crab submit '+crab_cfg)
		os.system('crab submit '+crab_cfg)


if __name__ == '__main__':
	if option.test:
		submit_multiple_crab_jobs(sample.testdict)
	else:
		submit_multiple_crab_jobs(sample.signaldict)
		submit_multiple_crab_jobs(sample.bkgdict)
		submit_multiple_crab_jobs(sample.ttbarbkgdict)
		submit_multiple_crab_jobs(sample.datadict)

