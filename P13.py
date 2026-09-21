import numpy as np
import pandas as pd
df = pd.read_csv('Sample_File.csv')
print(df.head())
df.to_json('Sample_File_json.json')
df = pd.read_json('Sample_File_json.json')
print(df)
df.to_excel('Sample_File_Excel.xls', index=False)
df = pd.read_excel('Sample_File_Excel.xls')
print(df)
df.to_csv('SampleFilegzip.gz', compression='gzip', index=False)
df = pd.read_csv('SampleFilegzip.gz', compression='gzip')
print(df)
