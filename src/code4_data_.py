import pandas as pd
import sys
sys.path.append('../src')

def import_csv (string):
    dataframe_orig = pd.read_csv(string,encoding = "ISO-8859-1")
    return dataframe_orig