import pandas as pd
import numpy as np


# 도미
bream_length = pd.read_csv("data/bream_length.csv")
bream_weight = pd.read_csv("data/bream_weight.csv")

# 빙어
smelt_length = pd.read_csv("data/smelt_length.csv")
smelt_weight = pd.read_csv("data/smelt_weight.csv")

# 전부 2차원 => ndarray타입
bream_length = bream_length.to_numpy()
bream_weight = bream_weight.to_numpy()
smelt_length = smelt_length.to_numpy()
smelt_weight = smelt_weight.to_numpy()

# 1차원으로 변경
bream_length = bream_length.flatten()
bream_weight = bream_weight.flatten()
smelt_length = smelt_length.flatten()
smelt_weight = smelt_weight.flatten()


fish_length = np.hstack((bream_length, smelt_length))
fish_weigth = np.hstack((bream_weight, smelt_weight))

# 피쉬 데이터로 한번에 합치기 - (2, 49) 2차원
fish_data = np.vstack((fish_length, fish_weigth))

# 피쉬 데이터 행 <-> 렬 치환하기 - (49, 2) 2차원
fish_data = np.transpose(fish_data)

fish_target = np.concatenate((np.ones(35), np.zeros(14)))

# 타겟 데이터 - 2차원 
fish_target = fish_target.reshape(49, -1)
#print(fish_target)

index = np.arange(49)
np.random.shuffle(index)
print(index)
print(index[:35])

# 35개
train_input = fish_data[index[:35]] # 훈련 데이터 (모델) broadCasting
train_target = fish_target[index[:35]] # 타겟 데이터(모델)

# 14개
test_input = fish_data[index[35:]] # 훈련 데이터(검증)
test_target = fish_target[index[35:]] # 타겟 데이터(검증)


def getTrains():
    trains = np.hstack((train_target, train_input))
    trains_DataFrame = pd.DataFrame(trains, columns=["train_target", "train_length", "train_weight"])

    return trains_DataFrame

def getTestes():
    testes = np.hstack((test_target, test_input))
    testes_DataFrame = pd.DataFrame(testes, columns=["test_target", "test_length", "test_weight"])

    return testes_DataFrame 