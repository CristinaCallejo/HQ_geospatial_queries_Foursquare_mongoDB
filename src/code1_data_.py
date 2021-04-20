import pandas as pd

def export_df_to_csv(dataframe):
    dataframe.to_csv('../data_processed/dfcompanies1_v1.csv',index = False)
    if True:
        print('Attention: Export succesfull')
        print("Attention: File exported correctly to '../data_processed/dfcompanies1_v1.csv'")

