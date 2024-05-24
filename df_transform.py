import pandas as pd 

class DataTransform:

    def __init__(self, df):
        self.df = df 

    def datetime_conversion(self, column):
        # column=pd.to_datetime(column, format='mixed',infer_datetime_format=True, errors='coerce')
        self.df[column]=pd.to_datetime(self.df[column], format='mixed')
        return self.df
   
    def category_conversion(self, column):
        self.df[column]=self.df[column].astype('category')
        return self.df

    def drop_cols(self, columns):
        self.df.drop(columns, axis=1, inplace=True)
        return self.df
    
    def drop_rows(self, column):
        self.df.dropna(subset=[column], inplace=True)
        return self.df
    
    def remove_strings(self, column):

        self.df[column]=self.df[column].str.extract(r'(\d+)', expand=False)
        self.df[column]=pd.to_numeric(self.df[column])
        return self.df[column]        

    def impute_median(self, column): 
        self.df[column].fillna(self.df[column].median(), inplace=True)
        return self.df
    
    def impute_mean(self,column):
        self.df[column].fillna(self.df[column].mean(), inplace=True)
        return self.df
