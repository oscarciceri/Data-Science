import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import json
import math 
import os
import random



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
print(size)