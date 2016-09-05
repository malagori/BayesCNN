__author__ = "Mehmood Alam Khan"
__email__  = "malagori@kth.se"
__version__= "0.9"
__credits__ = ["Muhammed Abdel Aziz", "Mehmood Alam Khan"]


from beneWrapper import BeneWrapper
from dataReader import DataReader

class MainWorkFlow(object):
    '''
    This class contains the main workflow of our algorithm
    '''
    vdFile      = None
    dataFile    = None
    outdir      = None
    alpha       = None
    def __init__(self, vdFile, dataFile, alpha, outDir):
        '''
        Constructor
        '''
        self.vdFile         = vdFile
        self.dataFile       = dataFile
        self.outDir         = outDir
        self.alpha          = alpha

    def runWorkFlow(self):
        '''
        This function instanciate bene class and run the bene software
        :return:
        '''
        objDataReader= DataReader()


        # read vd File
        variableNames, cardinality= objDataReader.returnVarNamesAndCardinalities(self.vdFile)

        # total number of variables
        totalVaiables= len(variableNames)

        # instantiate Benewrapper class
        objBeneWraper= BeneWrapper(self.vdFile, self.dataFile, self.alpha, self.outdir, totalVaiables)

        # generate optimum BNT using bene
        objBeneWraper.generateOptBnt()

        # read optimum BNT in a list of list format
        optimumBNT= objBeneWraper.readBeneBnt()

        # print optimum DAG
        print optimumBNT



