import pandas as pd
from sqlalchemy import create_engine
import yaml

def load_yaml_file():
    with open('credentials.yaml','r') as file:
        credentials=yaml.safe_load(file)
    return credentials    

def load_data_from_csv(file_name):
    df=pd.read_csv(file_name, index_col=0)
    return df


class RDSDatabaseConnector:

    def __init__(self, credentials):  
        """connection credentials from credentials.yaml config file. 
        Args:
            credentials in dictionary format
        """  
        self.credentials=load_yaml_file()

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

    def dataframe_to_csv(self, df, file_name):
        """dataframe to be saved in csv file format
        Args:
            dataframe : dataframe to be saved
            file_name : filename 
        """        
        return df.to_csv(file_name)




if __name__=="__main__":


    test=RDSDatabaseConnector(credentials)
    engine=test.initialise_db_engine()

    df=test.read_rds_table(engine,'loan_payments')
    print("df1", df.head(3))

    test.dataframe_to_csv(df, 'loan_payments.csv')
    print("********")

    df2=load_data_from_csv('loan_payments.csv')
    print("df2", df2.columns)





