### FWLJMET -- Full Framework LJMET (wrapper)



install:

	source /cvmfs/cms.cern.ch/cmsset_default.csh
	
	#from SLC7 (recommended)
	setenv SCRAM_ARCH slc7_amd64_gcc700
	cmsrel CMSSW_10_6_19
	cd CMSSW_10_6_19/src/
	
	
	cmsenv

	
	## Redo MET filter
	git cms-addpkg RecoMET/METFilters

	## HOT tagger part1
	git clone https://github.com/susy2015/TopTagger.git
	#### For top tagger, the current version at github is not compatible with CMSSW_10_6_19, the following modifications need to be made:
	###  In TopTagger/DataFormats/BuildFile.xml, add:
	## <use name="clhep"/>
	## <use name="root"/>
	###
	
	#### The old instruction for adding Axis1 information "git cms-merge-topic -u pastika:AddAxis1_1026" doesn't work for CMSSW_10_6_19, please do the following steps by hand:
	git cms-addpkg RecoJets/JetProducers
	### Then in RecoJets/JetProducers/plugins/QGTagger.cc, replace it with the one at https://github.com/jingyuluo/QG_SA/blob/master/QGTagger.cc
	### Also in RecoJets/JetProducers/interface/QGTagger.h, "std::tuple<int, float, float> calcVariables" should be replaced with "std::tuple<int, float, float, float> calcVariables"

	## EGamma post-reco for MVA values (NOTE: won't work in 10_2_9)
	git cms-merge-topic cms-egamma:EgammaPostRecoTools
	git cms-addpkg RecoEgamma/EgammaTools  ### essentially just checkout the package from CMSSW
	git clone https://github.com/cms-egamma/EgammaPostRecoTools.git
	mv EgammaPostRecoTools/python/EgammaPostRecoTools.py RecoEgamma/EgammaTools/python/.
	git clone -b ULSSfiles_correctScaleSysMC https://github.com/jainshilpi/EgammaAnalysis-ElectronTools.git EgammaAnalysis/ElectronTools/data/
	git cms-addpkg EgammaAnalysis/ElectronTools

	### BestCalc: copy lwtnn so that BestCalc.cc will compile.
	### This is not ideal, should always try to get official CMSSW / GitHub recipes whenever possible.
	### JH May 11: likely json needs to get remade by BEST team to use "lwtnn"-owned github. 
	### Dan Marley's lwtnn github linked below never tested...
	cp -r ~jmanagan/nobackup/CMSSW_9_4_12/src/lwtnn .   ## use scp after a Fermilab kinit to copy onto non-LPC clusters

	## Check out FWLJMET
	git clone -b 10_6_19_UL17 https://github.com/cms-ljmet/FWLJMET.git
	cd FWLJMET
	
	## Update the prefiring map for UL17 following https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1ECALPrefiringWeightRecipe, more specifically:
	git-cms-addpkg PhysicsTools/PatUtils 
	cd PhysicsTools/PatUtils/data/
	wget --no-check-certificate https://github.com/cms-data/PhysicsTools-PatUtils/raw/master/L1PrefiringMaps.root 


	## JetSubCalc currently uses uses PUPPI mass corrections:
	cd ${CMSSW_BASE}/src/FWLJMET/LJMet/data/
	git clone https://github.com/thaarres/PuppiSoftdropMassCorr

	cd -

	scram b

	## HOT tagger part2
	cd ${CMSSW_BASE}/src
	cmsenv
	mkdir -p ${CMSSW_BASE}/src/TopTagger/TopTagger/data
	getTaggerCfg.sh -o -n -t DeepResolved_DeepCSV_GR_noDisc_Release_v1.0.0 -d $CMSSW_BASE/src/TopTagger/TopTagger/data

	## Tprime/Bprime signal pdf change environment variable -- choose bash or csh version
	setenv LHAPDF_DATA_PATH "/cvmfs/cms.cern.ch/lhapdf/pdfsets/current/":${LHAPDF_DATA_PATH}  ## csh
	export LHAPDF_DATA_PATH="/cvmfs/cms.cern.ch/lhapdf/pdfsets/current/":${LHAPDF_DATA_PATH}  ## bash



Some info:

- LJMet/plugins/LJMet.cc : the EDAnalyzer that wraps LJMet classes
- Modified MET: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETUncertaintyPrescription#Instructions_for_9_4_X_X_9_or_10
- Redo MET filter : https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#How_to_run_ecal_BadCalibReducedM
- el ID V2 : https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2
- HOT tagger : https://github.com/susy2015/TopTagger/tree/master/TopTagger#instructions-for-saving-tagger-results-to-nanoaod-with-cmssw_9_4_11 (needs updating !)
- BoostedEventShapeTagger(BEST) :
     - https://bregnery.github.io/docs/BESTstandaloneTutorial/
     - https://github.com/justinrpilot/BESTAnalysis/tree/master
     - https://github.com/demarley/lwtnn/tree/CMSSW_8_0_X-compatible#cmssw-compatibility


run LJMet tester file:

    cmsRun LJMet/tester2017.py (or tester2016.py, or tester2018.py)

