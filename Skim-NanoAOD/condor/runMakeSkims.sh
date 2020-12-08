#!/bin/bash
#To be run on remote machine
#Take input arguments as an array
myArray=( "$@" )
#Array: Size=$#, an element=$1, all element = $@

printf "Start Running Histogramming at ";/bin/date
printf "Worker node hostname ";/bin/hostname

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then 
    echo "Running Interactively" ; 
else
    echo "Running In Batch"
    echo ${_CONDOR_SCRATCH_DIR}
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    scramv1 project CMSSW CMSSW_10_2_14
    cd CMSSW_10_2_14/src
    eval `scramv1 runtime -sh`
    cd ../..
	tar --strip-components=1 -zxvf Skim-NanoAOD.tar.gz
fi

#Run for Base, Signal region
echo "All arguements: "$@
echo "Number of arguements: "$#
year=$1
channel=$2
varname=${channel}_FileList_${year}
cd sample
source fileList_${year}.sh
cd -
echo "./makeSkim ${year} ${channel}_${year}_skim.root ${!varname}"
./makeSkim ${year} ${channel}_${year}_skim.root ${!varname}

printf "Done Histogramming at ";/bin/date
#---------------------------------------------
#Copy the ouput root files
#---------------------------------------------
condorOutDir=/store/user/rverma/Output/cms-hcs-run2/Skim-NanoAOD
if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then
    echo "Running Interactively" ;
else
    xrdcp -f ${channel}_${year}_skim.root root://cmseos.fnal.gov/${condorOutDir}/${year}
    echo "Cleanup"
    rm -rf CMSSW_10_2_14
    rm *.root
fi
printf "Done ";/bin/date
