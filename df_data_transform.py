import numpy as np
import numpy as np
from scipy.stats import boxcox, yeojohnson

class DataFrameTransform:

    def __init__(self, df):
        self.df = df

    def log_transform(self, column):
        """ This method transforms the values of the specified column using log transformation. 
        Args:
            column (str): the name of column to be transformed

        Returns:
            pandas.DataFrame: dataframe with the transformed column

        """        
        self.df[column].map(lambda i: np.log(i) if i > 0 else 0)
        return self.df
    
    def boxcox_transform(self, column):
        """ This method transformed the values of the specified column using Box-Cox transformation

        Args:
            column (str): the name of column to be transformed

        Returns:
            pandas.DataFrame: dataframe with the transformed column
        """        
        data=self.df[column]
        bc_pop=boxcox(data)
        self.df[column]=bc_pop[0]
        return self.df
    
    def yj_transform(self, column):
        """ This method transformed the values of the specified column using Yeo-Johnson transformation

        Args:
            column (str): the name of column to be transformed

        Returns:
            pandas.DataFrame: dataframe with the transformed column
        """    
        data=self.df[column]
        yj_pop=yeojohnson(data)
        self.df[column]=yj_pop[0]
        return self.df

    def handle_outliers(self, column):
        """ Handles outliers in the specified column of the Dataframe by Floowing and Capping them. 

        Args:
            column (str): the name of column to handle outliers for

        Returns:
            pandas.DataFrame: dataframe with outliers handled in the column specified.
        """   

        LQ=self.df[column].quantile(0.25) 
        UQ=self.df[column].quantile(0.75) 
        IQR = UQ-LQ
        threshold=1.5
        self.df.loc[(self.df[column] < LQ - threshold * IQR), column]=LQ
        self.df.loc[(self.df[column] > UQ + threshold * IQR), column]=UQ 
        return self.df      
