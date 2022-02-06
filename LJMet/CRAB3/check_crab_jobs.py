import os, argparse, imp

parser = argparse.ArgumentParser()
parser.add_argument( "-l", "--logs", action = "store", required = True )
parser.add_argument( "--resubmit", action ="store_true", default=False)
parser.add_argument( "--report", action ="store_true", default=False)
parser.add_argument( "--kill", action ="store_true", default=False)
parser.add_argument( "--verbose", action = "store_true" )
parser.add_argument( "--test", action = "store_true" )
option = parser.parse_args()

#Sample list file
postfix = option.logs.split( "_" )[1].strip("/")
sampleListPath = "sample_list_{}.py".format( postfix )
sample = imp.load_source( "Sample", sampleListPath, open(sampleListPath,"r") )

def check_crab_jobs( sample_dict ):
  for dataset in sample_dict:
    if option.resubmit:
      print( ">> Resubmitting {}: {}".format( dataset, sample_dict[dataset] ) )
      os.system( "crab resubmit {}".format( os.path.join( option.logs, "crab_{}".format( dataset ) ) ) )
    elif option.kill:
      print( ">> Killing {}: {} ".format( dataset, sample_dict[dataset] ) )
      os.system( "crab kill {}".format( os.path.join( option.logs, "crab_{}".format( dataset ) ) ) )
    else:
      print( ">> Checking status {}: {}".format( dataset, sample_dict[dataset] ) )
      if option.verbose:
        os.system( "crab status --verboseErrors {}".format( os.path.join( option.logs, "crab_{}".format( dataset ) ) ) )
      else:
        os.system( "crab status {}".format( os.path.join( option.logs, "crab_{}".format( dataset ) ) ) )

if __name__ == '__main__':
  if option.test:
    check_crab_jobs(sample.testdict)
  else:
    check_crab_jobs(sample.signaldict)
    check_crab_jobs(sample.bkgdict)
    check_crab_jobs(sample.ttbarbkgdict)
    check_crab_jobs(sample.datadict)

