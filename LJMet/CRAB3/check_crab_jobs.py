import os, argparse, imp

parser = argparse.ArgumentParser()
parser.add_argument( "-f", "--finalstate", action ="store", required = True )
parser.add_argument( "-y", "--year", action ="store", required = True )
parser.add_argument( "--resubmit", action ="store_true", default=False)
parser.add_argument( "--report", action ="store_true", default=False)
parser.add_argument( "--kill", action ="store_true", default=False)
parser.add_argument( "--verbose", action = "store_true" )
option = parser.parse_args()

#Sample list file
sampleListPath = "sample_list_{}20{}UL.py".format( option.finalstate, option.year )
samples = imp.load_source( "Sample", sampleListPath, open(sampleListPath,"r") )

def check_crab_jobs( sample_dict, crab_dir ):
  for dataset in sample_dict:
    if option.resubmit:
      print( ">> Resubmitting {}: {}".format( dataset, sample_dict[dataset] )
      os.system( "crab resubmit {}".format( os.path.join( crab_dir, "crab_UL{}_{}".format( option.year, sample ) ) ) )
    elif option.kill:
      print( ">> Killing {}: {} ".format( dataset, sample_dict[dataset] )
      os.system( "crab kill {}".format( os.path.join( crab_dir ) ) )
    else:
      print( ">> Checking status {}: {}".format( dataset, sample_dict[dataset] ) )
      os.system( "crab status {}".format( os.path.join( crab_dir, "crab_UL{}_{}".format( option.year, sample ) ) )


if __name__ == '__main__':

  check_status_multiple_crab_jobs(sample.signaldict)
  check_status_multiple_crab_jobs(sample.bkgdict)
  check_status_multiple_crab_jobs(sample.ttbarbkgdict)
  check_status_multiple_crab_jobs(sample.datadict)

