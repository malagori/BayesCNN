'''
Created on May 26, 2015

@author: Mehmood Alam Khan Malagori
@email:   malagori@kth.se
'''
__author__ = "Mehmood Alam Khan"
__email__  = "malagori@kth.se"
__version__= "0.9"
__credits__ = ["Mehmood Alam Khan"]

import copy
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

class PreProcessData(object):
    '''
    This class contains methods related to data pre-processing
    '''


    def __init__(self, df):
        '''
        Constructor
        '''
        self.df= copy.deepcopy(df.copy())

    def setDf(self,df):
        '''
        df setter
        '''
        self.df=  copy.deepcopy(df.copy())

    def getDf(self):
        '''
        df getter
        '''
        return self.df

    def fillMissingValuesByMean(self):
        '''
        This function will replace the missing values with mean values
        '''
        self.setDf(self.df.fillna(self.df.mean()))

    def normalizeDataByDailyConsumption(self):
        '''
            This function will normalize the data by daily consumption
        '''
        # minMaxScaler
        dfNorm = (self.df - self.df.min()) / (self.df.max() - self.df.min())
        #print self.df.sum(axis=1, skipna=True)
        #dfNorm= (self.df / self.df.sum(axis=1, skipna=True))
        #dfNorm = (self.df - self.df.mean()) / (self.df.max() - self.df.min())
        #print self.df
        self.setDf(dfNorm)

    #        print self.df[:].iloc[1:2]
    #        self.df[self.df.columns] = self.df[self.df.columns].apply(lambda x: StandardScaler().fit_transform(x))
    #        #self.df[self.df.columns] = self.df[self.df.columns].apply(lambda x: scale(x))
    #        print self.df[:].iloc[1:2]

    def scikitPCA(self, nComponents):
        '''
        PCA Using scikit-learn (based on SVD)
        '''
        # Standardize
        #standardizedDf = StandardScaler().fit_transform(self.df)

        # PCA
        sklearn_pca = PCA(n_components=nComponents)
        #transfomedDF = sklearn_pca.fit_transform(standardizedDf)
        transfomedDF = sklearn_pca.fit_transform(self.df)
        print (79 * '_')
        print "Variance explained by each PCA component"
        print (sklearn_pca.explained_variance_)
        print (79 * '_')
        # Plot the data
        plt.scatter(transfomedDF[:,0], transfomedDF[:,1])
        indexs=[i for i in xrange(0,transfomedDF.size)]
        for label, x, y in zip(indexs, transfomedDF[:, 0], transfomedDF[:, 1]):
            plt.annotate(
                label,
                xy = (x, y), xytext = (0.05, 0.05),
                textcoords = 'offset points', ha = 'right', va = 'bottom')#,
            #bbox = dict(boxstyle = 'round,pad=0.3', fc = 'white', alpha = 0.3),
            #arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
        plt.title('PCA via scikit-learn')
        #plt.show()
        plt.savefig('VisualizeData.pdf', bbox_inches='tight')



