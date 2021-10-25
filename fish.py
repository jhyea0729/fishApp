import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 도미
bream_length = pd.read_csv("data/bream_length.csv")

bream_weight = pd.read_csv("data/bream_weight.csv")

# 빙어
smelt_length = pd.read_csv("data/smelt_length.csv")

smelt_weight = pd.read_csv("data/smelt_weight.csv")

bream_data = np.column_stack((bream_length, bream_weight))
smelt_data = np.column_stack((smelt_length, smelt_weight))
print(bream_data)
print(smelt_data)


#plt.scatter(bream_length, bream_weight)
plt.scatter(bream_data[:,0], bream_data[:,1])
plt.scatter(smelt_data[:,0], smelt_data[:,1])
plt.xlabel("lenght")
plt.ylabel("weight")
plt.show()
