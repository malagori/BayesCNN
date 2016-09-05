#!/usr/bin/env python
__author__ = "Mehmood Alam Khan"
__email__  = "malagori@kth.se"
__version__= "0.9"
__credits__ = ["Muhammed Abdel Aziz", "Mehmood Alam Khan"]


import sys
import os
import datetime
import time
import tempfile
from optparse import OptionParser
from bayesCNN.randomSeed import RandomSeed
from bayesCNN.mainWorkFlow import MainWorkFlow



def gui(argv):
    usage = "usage: runBayesCNN [options]"
    description="""DESCRIPTION:     Believe me: This is a cool program!"""

    if len(argv) == 0:
        print usage
        sys.exit()

    parser = OptionParser(usage=usage, description=description )

    parser.add_option('-v', metavar='vdFilePath',
                      action='store' ,type="string", dest="vdFilePath",
                      help='Specify path to the file containing variable information ')
    parser.add_option('-d',metavar='dataFilePath',
                      action='store' ,type="string", dest="dataFilePath",
                      help='Specify path to the data file ')
    parser.add_option('-a', metavar='alpha',
                      action="store", type="float", dest="alpha",
                      help='Specify alpha parameter. Default=1.0', default=1.0)
    parser.add_option('-o', metavar='outDir',
                      action="store", type="string", dest="outDir",
                      help='Specify path to the output directory to store results files.')
    parser.add_option('-s', metavar='seed' ,
                      action="store", type="int", dest="seed",
                      help='Specify seed. default=121', default=121)
    parser.add_option('-l', metavar='loadSeed',
                        action='store' ,type="string", dest="loadSeed",
                        help='Specify path to a file containing previous state (default=None)', default=None)


    (options, args) = parser.parse_args()

    if options.outDir == None:
        options.outDir=tempfile.mkdtemp()
    elif os.path.exists(options.outDir) == False:
        os.mkdir(options.outDir)

    print "Output directory: %s"  % (options.outDir)
    seedNum         = options.seed
    # instantiating RandomSeed object
    rs=RandomSeed()

    if seedNum == None and options.loadSeed == None:
        seedNum= time.time()
    elif seedNum != None and options.loadSeed == None:
        rs.setInitialState(seedNum)
    elif options.loadSeed != None and seedNum == None:
        state= rs.getSateFromFile(options.loadSeed)
        rn.setstate(state)

    with open(options.outDir+"/out.bayesccn."+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S'))+".info", 'w') as wf:
        wf.write("Directory: %s\n" %(options.outDir))
        wf.write("Initial Seed: %d\n" %(seedNum))
        wf.write("VD File Path: %s\n" %(options.vdFilePath))
        wf.write("Data File Path: %s\n" %(options.dataFilePath))
        wf.write("Alpha : %s\n" %(options.alpha))
        wf.write("Load Seed File : %s\n" %(options.loadSeed))
        wf.write("TimeStamp : %s\n" %(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S'))))
    return options.vdFilePath, options.dataFilePath, options.alpha, options.outDir

def main(argv):
 
    # call gui function
    vdFilePath, dataFilePath, alpha, outDir= gui(argv)
    print "vd: %s " %(vdFilePath)
    print "datafi: %s " %(dataFilePath)
    print "alpha: %f " %(alpha)
    print "dir: %s " %(outDir)
    
    # run the name workflow
    print "-->bayesCNN starts"
    objMainWorkFlow= MainWorkFlow(vdFilePath, dataFilePath, alpha, outDir)
    objMainWorkFlow.runWorkFlow()
    print "-->bayesCNN ends"


if __name__ == '__main__':
    main(sys.argv[1:])