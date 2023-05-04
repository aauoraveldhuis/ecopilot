import pandas as pd
import os 
import matplotlib.pyplot as plt
import numpy as np


directory = r"C:\Users\Hamza\ecopilot"
os.chdir(directory)

df= pd.read_csv(r"C:\Users\Hamza\ecopilot\df.csv")
print(df.max())
print(df.min())

fig, axes = plt.subplots(nrows=3, ncols=1)



df['avstånd till framförvarande fordon (sek)'].plot(ax=axes[0])
axes[0].set_title('Avstånd till framförvarande fordon')
axes[0].set_ylabel('Avstånd (s)')




df['hastighet'].plot(ax=axes[1])
axes[1].set_title('Hastighet')
axes[1].set_ylabel('Hastighet (m/s)')


df['acc'].plot(ax=axes[2])
axes[2].set_title('Acceleration')
axes[2].set_xlabel('Tidssteg (0.2 s)')
axes[2].set_ylabel('Acceleration (m/s\u00B2) ')


plt.tight_layout()  # Adjusts the spacing between subplots
plt.show()