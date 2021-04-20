import pandas as pd
import requests 
import sys
sys.path.append('../src')

def import_csv (string):
    dataframe_orig = pd.read_csv(string,encoding = "ISO-8859-1")
    return dataframe_orig
def get_point(city):
    locat = requests.get(f"https://geocode.xyz/{city}?json=1").json()
    try:
        return {"type":"Point", "coordinates": [float(locat["longt"]), float(locat["latt"])]
        }
    except:
        return locat

def export_df_to_csv(dataframe):
    dataframe.to_csv("../data_processed/dataframe_v1.csv",index = False)
    if True:
        print('Attention: Export succesfull')
        print("Attention: File exported correctly")