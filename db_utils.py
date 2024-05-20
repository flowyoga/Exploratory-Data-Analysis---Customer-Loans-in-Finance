import pandas as pd
from sqlalchemy import create_engine
import yaml
# import os

# Task 2 Step 3 

with open('credentials.yaml','r') as file:
    credentials=yaml.safe_load(file)

# print(credentials)

# Task 1 Step 2
class RDSDatabaseConnector:

    # Task2 Steps 4 & 5
    def __init__(self, credentials):  
        """connection credentials from credentials.yaml config file. 
        Args:
            credentials in dictionary format
        """  
        self.credentials=credentials

    def initialise_db_engine(self):
        """initialise database engine 
        Returns:
            sqlalchemy connection engine 
        """        
        DBAPI='psycopg2'
        DATABASE=self.credentials['RDS_DATABASE']
        DATABASE_TYPE='postgresql'
        USER=self.credentials['RDS_USER']
        PASSWORD=self.credentials['RDS_PASSWORD']
        HOST=self.credentials['RDS_HOST']
        PORT=self.credentials['RDS_PORT']
        
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

        return engine

    # Task2 Step 6
    def read_rds_table(self, engine, table_name):      
        """
        Args:
            engine : database connection engine 
            table_name : table name that that needs to be loaded 
        Returns:
            data extract in dataframe
        """        
        query = r'select * from {}'.format(table_name)
        data=pd.read_sql_query(query, engine)
        return data

    # Task2 Step 7 

    def dataframe_to_csv(self, dataframe, file_name):
        """dataframe to be saved in csv file format
        Args:
            dataframe : dataframe to be saved
            file_name : filename 
        """        
        return dataframe.to_csv(file_name)
    
    # Task 3 

    def load_data_from_csv(self,  file_name):
        """load data from a local csv file 

        Returns:
           dataframe 
        """               
        df=pd.read_csv(file_name)
        return df
        

if __name__=="__main__":


    test=RDSDatabaseConnector(credentials)
    engine=test.initialise_db_engine()

    df=test.read_rds_table(engine,'loan_payments')
    print(df)

    test.dataframe_to_csv(df, 'loan_payments.csv')

    df2=test.load_data_from_csv('loan_payments.csv')
    print(df2)





