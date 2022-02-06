import os, argparse, imp

parser = argparse.ArgumentParser()
parser.add_argument( "-f", "--folder", required = True, help = "singleLep,doubleLep,multiLep" )
parser.add_argument( "--shifts", action = "store_true" )
parser.add_argument( "--test", action = "store_true" )
option = parser.parse_args()

#Sample list file
postfix = option.folder.split( "_" )[-1].strip("/") 
sampleListPath = "sample_list_{}.py".format( postfix )
sample = imp.load_source( "Sample", sampleListPath, open(sampleListPath,"r") )

home = os.environ['HOME']
CRABCONFIG_DIR = option.folder

def submit_crab_jobs( sample_dict, shifts ):
  for dataset in sample_dict:
    print( "Submitting {}: {}".format( dataset, sample_dict[ dataset ] ) )
    if shifts:
      crab_cfg = os.path.join( CRABCONFIG_DIR, "crab_config_shifts_{}.py".format( dataset ) )
    else:
      crab_cfg = os.path.join( CRABCONFIG_DIR, "crab_config_{}.py".format( dataset ) )
    
    os.system( "crab submit {}".format( crab_cfg ) )
    

if __name__ == '__main__':
  if option.test:
    submit_crab_jobs(sample.testdict,option.shifts)
  else:
    submit_crab_jobs(sample.signaldict,option.shifts)
    submit_crab_jobs(sample.bkgdict,option.shifts)
    submit_crab_jobs(sample.ttbarbkgdict,option.shifts)
    submit_crab_jobs(sample.datadict,option.shifts)
