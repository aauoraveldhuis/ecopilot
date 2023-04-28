import pandas as pd
import os 


directory = r"C:\Users\Hamza\ecopilot"
os.chdir(directory)

df= pd.read_csv(r"C:\Users\Hamza\ecopilot\df.csv")
print(df.max())
print(df.min())
