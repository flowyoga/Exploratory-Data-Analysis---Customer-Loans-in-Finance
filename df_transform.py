import pandas as pd 

class DataTransform:

    def __init__(self, df):
        self.df = df 

    def datetime_conversion(self, column):  
        """ converts the values in the specified column to datetime format.

        Args:
            column (str): column to be checked

        Returns:
            dataframe with the column converted
        """             
        self.df[column]=pd.to_datetime(self.df[column], format='mixed')
        return self.df
   
    def category_conversion(self, column):
        """ converts the values in the specified column to categorical type.

        Args:
            column (str): column tob e checked

        Returns:
            dataframe with the column converted
        """        
        self.df[column]=self.df[column].astype('category')
        return self.df

    def drop_cols(self, columns):
        """ drops the specified column from the dataframe

        Args:
            columns (str): column to be dropped

        Returns:
            updated dataframe
        """        
        self.df.drop(columns, axis=1, inplace=True)
        return self.df
    
    def drop_rows(self, column):
        """ drops rows with missing values in the specified column.

        Args:
            column (str): column name where missing values need to be checked

        Returns:
            updated dataframe
        """        
        self.df.dropna(subset=[column], inplace=True)
        return self.df
    
    def remove_strings(self, column):
        """ removes non-numeric characters from the values in the specified column.

        Args:
            column (str): column name

        Returns:
            updated dataframe
        """
        self.df[column]=self.df[column].str.extract(r'(\d+)', expand=False)
        self.df[column]=pd.to_numeric(self.df[column])
        return self.df[column]        

    def impute_median(self, column): 
        """ imputes missing values in the specified column with the median value.
        Args:
            column (str): column name 

        Returns:
            updated dataframe
        """        
        self.df[column].fillna(self.df[column].median(), inplace=True)
        return self.df
    
    def impute_mean(self,column):
        """ imputes missing values in the specified column with the mean value.
        Args:
            column (str): column name 

        Returns:
            updated dataframe
        """ 
        self.df[column].fillna(self.df[column].mean(), inplace=True)
        return self.df
