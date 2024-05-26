class DataFrameInfo:

    def __init__(self, df):
        self.df = df 

    def df_info(self, column_name):
        return self.df[column_name].info()

    def df_describe(self, column_name):
        return self.df[column_name].describe()
    
    def df_unque_value_counts(self,  column_name):
        return self.df[column_name].value_counts()
    
    def df_shape_check(self):
        return self.df.shape 
    
    def null_value_check(self): 
        column_inc_null_values=self.df.columns[self.df.isnull().any()]
        percentage_checked={}

        for column in column_inc_null_values:
            percentage_checked[column]=round(self.df[column].isnull().sum()/len(self.df)*100,2)

        return percentage_checked    
    
    def remove_strings(self, column):
        substrings_to_remove=['months', '+', '<', 'year', 'years']

        for substring in substrings_to_remove:
            self.df[column]=self.df[column].str.replace(substring,' ')
        return self.df[column]    
    
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
