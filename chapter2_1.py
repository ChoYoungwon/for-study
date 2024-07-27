import time
import random
import pandas as pd
import matplotlib.pyplot as plt

ls = [0]*100
def MakeList():
    for i in range(100):
        ls[i] = random.randint(0, 10000)
    return

def algorithmA():
    MakeList()
    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            if ls[i] == ls[j]:
                return True
    return False

def algorithmB():
    MakeList()
    ls.sort()
    for i in range(len(ls)-1):
        if ls[i] == ls[i+1]:
            return True
    return False

A = []
B = []
Input = [i for i in range(0, 50000, 5000)]
for k in Input:
    start = time.time()
    for _ in range(k):
        algorithmA()
    end = time.time()
    resultA = end - start
    print("실행시간 = ", resultA)
    A.append(resultA)

    start = time.time()
    for _ in range(k):
        algorithmB()
    end = time.time()
    resultB = end - start
    print("실행시간 = ", resultB)
    B.append(resultB)

data = {'A': A, 'B': B}

df = pd.DataFrame(data, index = Input)
df.plot()
plt.show()


