import random

def gcd(a, b):
    alist = []
    blist = []
    #  공약수를 리스트(alist, blist)에 저장
    for i in range(a):
        i += 1
        if a % i == 0:
            alist.append(i)
    for k in range(b):
        k += 1
        if b % k == 0:
            blist.append(k)

    # 약수를 비교해 최대공약수를 구한다
    if len(alist) < len(blist):
        for i in range(len(alist)):
            for j in range(len(blist)):
                if alist[i] == blist[j]:
                    max_pcd = alist[i]
                    break
    else:
        for i in range(len(blist)):
            for j in range(len(alist)):
                if alist[j] == blist[i]:
                    max_pcd = alist[j]
                    break

    print(f'{a}의 약수 = ', alist)
    print(f'{b}의 약수 = ', blist)
    print(f'{a}과 {b}의 최대 공약수 = ', max_pcd)
    print('\n')
    return

for _ in range(5):
    gcd(random.randrange(60)+1, random.randrange(60)+1)
