import random                   # 흰 구슬과 검은 구슬의 개수를 설정하기 위해 사용
n = random.randint(1, 10)   # 흰 구슬(1)과 검은 구슬(0)의 각자 개수 : n
ls = [0]*n + [1]*n           # 리스트에 총 2n개의 구슬 저장 (2~20개)
random.shuffle(ls)           # 리스트의 원소를 무작위로 섞는다(shuffle)
print(ls)

# 중간 까지 도달 했을 때 모두 왼쪽은 모두 흰 구슬로 채워 지므로 리스트의 절반만 탐색
for i in range(len(ls)//2):
    k = i                    # 변수 k를 이용해 인덱스를 변화 시킨다.
    while k < len(ls):       # 흰 구슬의 위치를 찾는 내부 반복문
        if ls[k] != 1:
            k += 1
        else:                # 흰 구슬을 찾은 경우 반복문을 나온다.
            break
    # i : 현재 위치, k : 가장 가까운 흰 구슬의 위치
    # i가 흰 구슬인 경우 : (i == k)
    while k > i:
        ls[k], ls[k-1] = ls[k-1], ls[k]
        print(ls)
        k -= 1