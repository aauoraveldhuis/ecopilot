import pandas as pd
import os 
import matplotlib.pyplot as plt


directory = r"C:\Users\Hamza\ecopilot"
os.chdir(directory)

df= pd.read_csv(r"C:\Users\Hamza\ecopilot\df.csv")
print(df.max())
print(df.min())

fig, axes = plt.subplots(nrows=3, ncols=1)

df['avstånd till framförvarande fordon (sek)'].plot(ax=axes[0])
axes[0].set_title('Distance to Leading Vehicle')
axes[0].set_ylabel('Distance (sec)')

df['hastighet'].plot(ax=axes[1])
axes[1].set_title('Speed')
axes[1].set_ylabel('Speed (units)')

df['acc'].plot(ax=axes[2])
axes[2].set_title('Acceleration')
axes[2].set_xlabel('Time')
axes[2].set_ylabel('Acceleration (units)')

plt.tight_layout()  # Adjusts the spacing between subplots
plt.show()