import pandas as pd
import os 
import matplotlib.pyplot as plt

directory = r"C:\Users\Hamza\ecopilot"
os.chdir(directory)

df= pd.read_csv(r"C:\Users\Hamza\ecopilot\df.csv")
df.dropna()

print(df.min())
print(df.max())

fig, axes = plt.subplots(nrows=3, ncols=1)

df['avstånd till framförvarande fordon (sek)'].plot(ax=axes[0])
df['hastighet'].plot(ax=axes[1])
df['acc'].plot(ax=axes[2])

plt.show()



