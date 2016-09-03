__author__ = "Mehmood Alam Khan"
__email__  = "malagori@kth.se"
__version__= "0.9"
__credits__ = ["Muhammed Abdel Aziz", "Mehmood Alam Khan"]

class DataReader(object):
    '''
    This class constains all the functions related to I/O
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def returnVarNamesAndCardinalities(infile):

        tokens=[]
        cardinality=[]
        variableNames=[]
        try:
            with open(infile, 'r') as f:
                for line in f:
                    tokens=line.split("\t")
                    variableNames.append(tokens[0])
                    cardinality.append(len(tokens)-1)
        except IOError:
            print "file: readVdFile; Function readVdFile();  Error: could not read vd file"

        return variableNames, cardinality
