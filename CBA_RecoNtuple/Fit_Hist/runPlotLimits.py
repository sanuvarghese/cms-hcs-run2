import os
import itertools
import json
from FitInputs import *

def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

for year, decay, channel in itertools.product(Year, Decay, Channel): 
    hName = "presel_Njet"
    dirDC = "%s/Fit_Hist/%s/%s/%s/%s/SR"%(condorCBADir, year, decay, channel, hName)
    nameDC = "mH*/higgsCombine_hcs_run2.AsymptoticLimits.mH*.root" 
    #runCmd("%s/%s"%(dirDC, nameDC))
    print hName
    runCmd("combineTool.py -M CollectLimits %s/%s -o %s/limits.json"%(dirDC, nameDC, dirDC))
    title_right = "35.9 fb^{-1} (13 TeV)"
    if "16" in year:
        title_right = "35.9 fb^{-1} (2016) (13 TeV)"
    if "17" in year:
        title_right = "41.5 fb^{-1} (2017) (13 TeV)"
    if "18" in year:
        title_right = "59.7 fb^{-1} (2018) (13 TeV)"
    title_left = "e + jets"
    if "Mu" in channel:
        title_left = "#mu + jets"
    out = "limit_%s_%s"%(year, channel)
    #runCmd("python plotLimits.py --title-left \"%s\" --title-right \"%s\" %s/limits.json -o %s/limits"%(title_left, title_right, dirDC, dirDC))
    runCmd("python plotLimits.py --title-left \"%s\" --title-right \"%s\" %s/limits.json -o %s"%(title_left, title_right, dirDC, out))
    #print args
