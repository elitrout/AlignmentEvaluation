'''
Created on Feb 10, 2015

@author: joro
'''
import sys
from PraatVisualiser import addAlignmentResultToTextGridFIle, tokenList2TabFile
from WordLevelEvaluator import determineSuffix, loadDetectedTokenListFromMlf
import os
from tab2PraatAndOpenWithPRaat import tab2PraatAndOpenWithPRaat

def mlfResult2TextGrid(argv):
    '''
    open mlf in praat. 
    '''
    if len(argv) != 3 :
            print ("  usage: {}  <detectedHTK_URI> <whichLevel>".format(argv[0]) )
            sys.exit();
    detectedHTK_URI= argv[1]
    whichEvalLevel =  int(argv[2])
    
    tokenAlignedSuffix, dummy = determineSuffix(withDuration=False, withSynthesis='dummy', evalLevel=whichEvalLevel)
    
    # load result from file into python list
    detectedTokenList = loadDetectedTokenListFromMlf( detectedHTK_URI, whichEvalLevel )
    
        # write to tsv file.  praat can open only tsv-s
    baseNameAudioFile = os.path.splitext(detectedHTK_URI)[0]
    tokenAlignedfileName =  tokenList2TabFile(detectedTokenList, baseNameAudioFile, tokenAlignedSuffix)
    
    tab2PraatAndOpenWithPRaat(['dummy', tokenAlignedfileName])

    
if __name__ == '__main__':
    mlfResult2TextGrid(sys.argv)

#     mlfResult2TextGrid([ 'dummy', "/tmp/02_Koklasam_3_zemin.htkAlignedMlf"])