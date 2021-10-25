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


fish_length = np.vstack((bream_length, smelt_length))
fish_weight = np.vstack((bream_weight, smelt_weight))
fish_data = np.vstack((bream_data, smelt_data))
fish_target = np.concatenate((np.ones(35), np.zeros(14)))

print(fish_target)
#print(fish_target.shape) # 합친 개수 = 도미의 개수 + 빙어의 개수

# fish_data, fish_target으로 셔플해서 test_target 구하기
index = np.arange(49) # 35(도미), 14(빙어)
np.random.shuffle(index)
print(index)

# 35개
train_input = fish_data[index[:35]] # 훈련 데이터 (모델) broadCasting
train_target = fish_target[index[:35]] # 타겟 데이터(모델)

# 14개
test_input = fish_data[index[35:]] # 훈련 데이터(검증)
test_target = fish_target[index[35:]] # 타겟 데이터(검증)


plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(test_input[:,0], test_input[:,1])
plt.xlabel("length")
plt.ylabel("weigth")
plt.show()

