import random

def gcd(a, b):
    alist = []
    for i in range(a):
        i += 1
        if a % i == 0:
            alist.append(i)
    alist.reverse()             # 큰 수부터 나누기 위해 사용
    for i in alist:
        if b % i == 0:
            max_pcd = i
            break
    alist.reverse()
    print(f'{a}의 약수 = ', alist)
    print(f'{a}과 {b}의 최대 공약수 = ', max_pcd)
    print('\n')
    return

for _ in range(5):
    gcd(random.randrange(60)+1, random.randrange(60)+1)