#!/usr/bin/env python
__author__ = "Mehmood Alam Khan"
__email__  = "malagori@kth.se"
__version__= "0.9"
__credits__ = ["Mehmood Alam Khan","Muhammed Abdel Aziz"]


import sys
import os
import datetime
import time
import tempfile
from optparse import OptionParser



def main(argv):

    usage = "usage: runBayesCNN [options]"
    description="""DESCRIPTION:     Believe me: This is a cool program!"""

    if len(argv) == 0:
        print usage
        sys.exit()

    parser = OptionParser(usage=usage, description=description )

    parser.add_option('-V', metavar='vdFilePath',
                      action='store' ,type="string", dest="vdFilePath",
                      help='Specify path to the file containing variable information ')
    parser.add_option('-d',metavar='dataFilePath',
                      action='store' ,type="string", dest="dataFilePath",
                      help='Specify path to the data file ')
    parser.add_option('-a', metavar='alpha',
                      action="store", type="float", dest="alpha",
                      help='Specify alpha parameter. Default=1.0', default=1.0)
    parser.add_option('-D', metavar='outDir',
                      action="store", type="string", dest="outDir",
                      help='Specify path to the output directory to store results files.')




    (options, args) = parser.parse_args()

    if options.outDir == None:
        options.outDir=tempfile.mkdtemp()
    elif os.path.exists(options.outDir) == False:
        os.mkdir(options.outDir)

    print "Output directory: %s"  % (options.outDir)

    with open(options.outDir+"/out.bayesccn."+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-h%H-m%M'))+".info", 'w') as wf:
        wf.write("Directory: %s\n" %(options.outDir))
        wf.write("VD File Path: %s\n" %(options.vdFilePath))
        wf.write("Data File Path: %s\n" %(options.dataFilePath))
        wf.write("Alpha : %s\n" %(options.alpha))
        wf.write("TimeStamp : %s\n" %(options.dataFilePath))



    print "-->bayesCNN starts"
    objMainWorkFlow= MainWorkFlow(options.vdFilePath, options.dataFilePath, options.alpha, options.outDir)
    objMainWorkFlow.runWorkFlow()
    print "-->bayesCNN ends"


if __name__ == '__main__':
    main(sys.argv[1:])