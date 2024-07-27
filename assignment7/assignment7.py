import random
import numpy as np

# 억지기법 알고리즘

def string_matching(T, P):
    number = 0
    for i in range(len(T)-len(P)+1):
        k = 0
        for j in range(len(P)):
            if T[i+j] != P[j]:
                number += 1
                print(f'{T[i+j]}와 {P[j]}를 서로 비교, 비교 횟수 : {number}')
                break
            else:
                number += 1
                print(f'{T[i + j]}와 {P[j]}를 서로 비교, 비교 횟수 : {number}')
                k += 1
        if k == len(P):
            return i
    return -1
NO_OF_CHARS = 128
def shift_table(pat):
    m = len(pat)
    tbl = [m]*NO_OF_CHARS

    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i

    return tbl

def search_horspool(T, P):
    m = len(P)
    n = len(T)
    t = shift_table(P)
    i = m-1
    num = 0
    while(i <= n-1):
        k = 0
        while k <= m-1 and P[m-1-k] == T[i-k]:
            num += 1
            print(f'{T[i-k]}와 {P[m-1-k]}를 서로 비교, 비교 횟수 : {num}')
            k += 1
        if k == m:
            return i-m+1
        else:
            num += 1
            print(f'{T[i - k]}와 {P[m - 1 - k]}를 서로 비교, 비교 횟수 : {num}')
            tc = t[ord(T[i-k])]
            num += 1
            print(f'{tc}만큼 이동, 횟수 : {num}')
            i += max(1, (tc-k))
            print(f'i의 값 : {i}')
    return -1


pattern = input("패턴을 입력해 주세요(대문자로 입력) : ")
# random_string = np.random.randint(65, 91, 2000)
# T_list = []
# for i in range(len(random_string)):
#     T_list.append(chr(random_string[i]))
# Text = "".join(T_list)

# Text = "I_LOVE_BANANA_YOU_LIKE_APPLE_AND_MANGO"
# Text = "AAAAAAAAB"
Text = "AAAAAABAA"
print("텍스트 : ", Text)
print('<억지기법>')
print(string_matching(Text, pattern))
print('\n<호스풀 알고리즘>')
print(search_horspool(Text, pattern))
