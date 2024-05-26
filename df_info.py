class DataFrameInfo:

    def __init__(self, df):
        self.df = df 

    def df_info(self, column): 
        """  displays the summary information of the specified column in the DataFrame.

        Args:
            column (str): column to be checked.

        Returns:
            column information 
        """        
        return self.df[column].info()

    def df_describe(self, column):

        """ generates descriptive statistics of the specified column. 

        Args: 
            column (str): column to be checked.

        Returns:
        descriptive statistics of the column   
            
        """        
        return self.df[column].describe()
    
    def df_unque_value_counts(self,  column):
        """ computes the counts of unique values in the column specified.

        Args:
            column (str): column to be checked.

        Returns:
            series containing the counts of unique values in the specified column.
        """        
        return self.df[column].value_counts()
    
    def df_shape_check(self):
        """ returns the dimension of a dataframe

        Returns:
            dimension of a dataframe
        """        
        return self.df.shape 
    
    def null_value_check(self): 
        """ checks for null values in the dataframe

        Returns:
            percentage of null values in each column if null value exists.
        """        
        column_inc_null_values=self.df.columns[self.df.isnull().any()]
        percentage_checked={}

        for column in column_inc_null_values:
            percentage_checked[column]=round(self.df[column].isnull().sum()/len(self.df)*100,2)

        return percentage_checked    
    
if __name__=="__main__":
    from db_utils import load_data_from_csv

    file_name='loan_payments_from_source.csv'
    df = load_data_from_csv(file_name)
    print(df.info())
    print(df.columns)
    h=DataFrameInfo(df)
    print(h.df_describe('loan_status'))
    print("shape check ", h.df_shape_check)
    print("null columns checks", h.null_value_check())
