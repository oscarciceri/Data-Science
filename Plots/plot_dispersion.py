import pandas as pd
import numpy as np
import seaborn as sns
import json
import math 
import os
import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm


name="dispersion_dataset.in"
print(name)
fname="/home/oscar/git/Data-Science/Plots/"+name
f = open(fname, 'r')
num_cols = len(f.readline().split('	'))
f.seek(0)
lines = f.read().splitlines()
f.close()

lines.pop(0)
size = len(lines)


date = []
apple = []
google = []
bankAmerica = []

# for i in range(len(lines)):
for i in range(50):
    data = lines[i].split('	')
    date.append(str(data[0].replace(',', '.')))
    apple.append(str(data[1].replace(',', '.')))
    google.append(str(data[2].replace(',', '.')))
    bankAmerica.append(str(data[3].replace(',', '.')))
print(google[1])






# Fixing random state for reproducibility
np.random.seed(19680801)
# N = len(google)
# colors = np.random.rand(N)
# area = (10 * np.random.rand(N))**2  # 0 to 15 point radii


len(apple)
len(google)

# matplotlib.axes.Axes.set_xscale(1, 'linear')


x = np.array(apple)
y = np.array(google)


plt.scatter(x, y, alpha=0.5, cmap=cm.Paired, marker='.')
plt.xlabel("Google") # Text for X-Axis
plt.ylabel("Apple") # Text for Y-Axis
plt.title("Relationship between Google and Applle")

plt.show()