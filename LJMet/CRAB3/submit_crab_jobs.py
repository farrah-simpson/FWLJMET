import os, argparse, imp

parser = argparse.ArgumentParser()
parser.add_argument( "-f", "--folder", required = True, help = "singleLep,doubleLep,multiLep" )
parser.add_argument( "-g", "--groups", nargs = "+", required = True )
parser.add_argument( "--shifts", action = "store_true" )
parser.add_argument( "--dryrun", action = "store_true" )
option = parser.parse_args()

#Sample list file
postfix = option.folder.split( "_" )[-1].strip("/") 
sampleListPath = "sample_list_{}.py".format( postfix )
samples = imp.load_source( "Sample", sampleListPath, open(sampleListPath,"r") )

home = os.environ['HOME']
CRABCONFIG_DIR = option.folder

def submit_crab_job( group, process, shifts, failed_submissions ):
  if shifts:
    crab_cfg = os.path.join( CRABCONFIG_DIR, "crab_config_shifts_{}.py".format( process ) )
  else:
    crab_cfg = os.path.join( CRABCONFIG_DIR, "crab_config_{}.py".format( process ) )
  if option.dryrun:
    try: 
      os.system( "crab submit --dryrun {}".format( crab_cfg ) )
    except:
      pass
  else:
    try: 
      os.system( "crab submit {}".format( crab_cfg ) )
    except:
      failed_submissions.append( process )

if __name__ == '__main__':
  print( "[START] Submitting CRAB3 jobs" )
  count = 0
  failed_submissions = []
  for group in option.groups:
    print( ">> Submitting jobs for {}".format( group ) )
    if group not in list( samples.groups.keys() ):
      print( "[WARN] {} is not a valid group listed in 'sample_list_{}{}UL.py'. Skipping.".format( group, option.finalState, option.year ) )
    else:
      for process in samples.groups[ group ]:
        print( "   + {}: {}".format( process, samples.groups[ group ][ process ].split("/")[1] ) )
        submit_crab_job( group, process, option.shifts, failed_submissions )
        count += 1
  if len( failed_submissions ) > 0:
    print( "[WARN] {} submissions failed, please check the naming or availability on GrASP or DAS:" )
    for submission in failed_submissions:
      print( "   - {}".format( submission ) )
  print( "[DONE] Submitted {} CRAB jobs.".format( count ) )

