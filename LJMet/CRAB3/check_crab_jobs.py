import os, argparse, imp

parser = argparse.ArgumentParser()
parser.add_argument( "-l", "--logs", action = "store", required = True )
parser.add_argument( "-g", "--groups", nargs = "+", required = True )
parser.add_argument( "--resubmit", action ="store_true", default=False)
parser.add_argument( "--report", action ="store_true", default=False)
parser.add_argument( "--kill", action ="store_true", default=False)
parser.add_argument( "--shift", action = "store_true" )
parser.add_argument( "--verbose", action = "store_true" )
option = parser.parse_args()

#Sample list file
postfix = option.logs.split( "_" )[1].strip("/")
sampleListPath = "sample_list_{}.py".format( postfix )
sample = imp.load_source( "Sample", sampleListPath, open(sampleListPath,"r") )

def check_crab_job( group, process ):
  if option.resubmit:
    print( "   + Resubmitting {}: {}".format( process, samples.groups[ group ][ process ] ) )
    os.system( "crab resubmit {}".format( os.path.join( option.logs, "crab_{}".format( process ) ) ) )
  elif option.kill:
    print( "   + Killing {}: {} ".format( process, samples.groups[ group ][ process ] ) )
    os.system( "crab kill {}".format( os.path.join( option.logs, "crab_{}".format( process ) ) ) )
  else:
    print( "   + Checking status {}: {}".format( process, samples.groups[ group ][ process ] ) )
    if option.verbose:
      os.system( "crab status --verboseErrors {}".format( os.path.join( option.logs, "crab_{}".format( process ) ) ) )
    else:
      os.system( "crab status {}".format( os.path.join( option.logs, "crab_{}".format( process ) ) ) )

if __name__ == '__main__':
  print( "[START] Checking CRAB3 jobs" )
  count = 0
	for group in option.groups:
    print( ">> Checking jobs for {}".format( group ) )
		if group not in list( samples.groups.keys() ):
			print( "[WARN] {} is not a valid group listed in 'sample_list_{}{}UL.py'. Skipping.".format( group, option.finalState, option.year ) )
		else:
			for process in sample.groups[ group ]:
				check_crab_job( group, process, option.shifts )
        count += 1
  print( "[DONE] Checked {} CRAB jobs.".format( count ) )

