import os, argparse, imp

parser = argparse.ArgumentParser()
parser.add_argument( "-f", "--finalState", required = True, help = "singleLep,doubleLep,multiLep" )
parser.add_argument( "-y", "--year", required = True, help = "16APV,16,17,18" )
parser.add_argument( "--shifts", action = "store_true" )
parser.add_argument( "--test", action = "store_true" )
option = parser.parse_args()

#Sample list file
sampleListPath = "sample_list_{}20{}UL.py".format( option.finalState, option.year )
sample = imp.load_source( "Sample", sampleListPath, open(sampleListPath,"r") )

home = os.environ['HOME']
CRABCONFIG_DIR = "crab_configs_{}20{}UL".format( option.finalState, option.year )

def submit_crab_jobs( sample_dict, shifts ):
  for dataset in sample_dict:
    print( "Submitting {}: {}".format( dataset, sample_dict[ dataset ] ) )
    if shifts:
      crab_cfg = os.path.join( CRABCONFIG_DIR, "crab_config_{}.py".format( dataset ) )
    else:
      crab_cfg = os.path.join( CRABCONFIG_DIR, "crab_config_shifts_{}.py".format( dataset ) )
    
    os.system( "crab submit {}".format( crab_cfg ) )
    

if __name__ == '__main__':
  if option.test:
    submit_crab_jobs(sample.testdict)
  else:
    submit_crab_jobs(sample.signaldict)
    submit_crab_jobs(sample.bkgdict)
    submit_crab_jobs(sample.ttbarbkgdict)
    submit_crab_jobs(sample.datadict)
