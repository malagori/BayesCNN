__author__ = "Mehmood Alam Khan"
__email__  = "malagori@kth.se"
__version__= "0.9"
__credits__ = ["Muhammed Abdel Aziz", "Mehmood Alam Khan"]

import pandas as pd
import copy

class DataReader(object):
    '''
    This class constains all the functions related to I/O
    '''

    df              = None
    variableNames   = None
    cardinality     = None

    def __init__(self):
        '''
        Constructor
        '''
        self.df             = pd.DataFrame(index=None, columns=None)
        self.cardinality    = []
        self.variableNames  = []

    def setCardinality(self, cardi):
        self.cardinality = cardi

    def setVariablNames(self, varNames):
        self.variableNames= varNames

    def setDf(self,df):
        self.df = copy.deepcopy(df.copy())

    def getCardinality(self, cardi):
        return  self.cardinality

    def getVariablNames(self, varNames):
        return  self.variableNames

    def getDf(self):
        return self.df

    def returnVarNamesAndCardinalities(self, infile):

        tokens=[]

        cardinality    = []
        variableNames  = []

        try:
            with open(infile, 'r') as f:
                for line in f:
                    tokens=line.split("\t")
                    variableNames.append(tokens[0])
                    cardinality.append(len(tokens)-1)
        except IOError:
            print "file: readVdFile; Function readVdFile();  Error: could not read vd file"

        self.setCardinality(cardinality)
        self.setVariablNames(variableNames)

    def readDataFrame(self,infile):
        """
        Read data from file containing dataframe in following format:
           H    A    B    C    D    E
           h1   0.1  0.3  1.2  0.4  0.4
           h2   1.2  1.1  1.5  1.6  1.3
           h3   2.0  1.4  0.1  0.2  0.3
        """
        try:
            df=pd.read_csv(infile)
            #newCols= [i for i in xrange(0, df.shape[1])]
            #df.columns= newCols
            self.setDf(df)
        except IOError:
            print "Class: DataReader; Function readDataFrame(); Error: could not read csv file"
