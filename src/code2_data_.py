import pandas as pd
import sys
sys.path.append('../src')

def import_csv (string):
    dataframe_orig = pd.read_csv(string,encoding = "ISO-8859-1")
    return dataframe_orig

def export_df_to_csv(dataframe):
    dataframe.to_csv("../data_processed/dfcompanies1_v2.csv",index = False)
    if True:
        print('Attention: Export succesfull')
        print("Attention: File exported correctly to '../data_processed/dfcompanies1_v2.csv'")
