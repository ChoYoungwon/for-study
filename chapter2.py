import time
import random

ls = [0]*100
def MakeList():
    for i in range(100):
        ls[i] = random.randint(0, 10000)
    return

def algorithmA():
    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            if ls[i] == ls[j]:
                return True
    return False

def algorithmB():
    ls.sort()
    for i in range(len(ls)-1):
        if ls[i] == ls[i+1]:
            return True
    return False

for i in range(20):
    MakeList()
    if algorithmA() == algorithmB():
        print("True")

