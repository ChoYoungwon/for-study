import random
import math

# 두 점 사이의 거리를 반환
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# 억지기법을 사용한 최단 거리 찾기
def closest_pair_solution(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])
            if dist < mindist:
                mindist = dist
    return p, mindist

def strip_closet_solution(P, d):
    n = len(P)
    d_min = d
    # P.sort(key = lambda point: point[1])    (정렬 제거)

    # 시간 복잡도 : O(n) / 내부 while 반복문은 상수 시간이 걸린다.
    for i in range(n):
        j = i + 1
        while j < n and (P[j][1] - P[i][1]) < d_min:
            dij = distance(P[i], P[j])
            if dij < d_min:
                d_min = dij
            j += 1
    return d_min

# y기준으로 리스트를 병합정렬한다 / 시간 복잡도 : O(n)
def merge(A, B):
    sorted = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i][1] <= B[j][1]:
            sorted.append(A[i])
            i += 1
        elif A[i][1] > B[j][1]:
            sorted.append(B[j])
            j += 1
    while i < len(A):
        sorted.append(A[i])
        i += 1
    while j < len(B):
        sorted.append(B[j])
        j += 1
    return sorted

def closest_pair_dist_solution(P, n):
    if n <= 3:
        P.sort(key=lambda point: point[1])      # 원소가 3개 이하로 y축 기준 정렬에 상수 시간이 걸린다.
        return P, closest_pair_solution(P)[1]
    mid = n // 2
    mid_x = P[mid][0]

    P[:mid], dl = closest_pair_dist_solution(P[:mid], mid)
    P[mid:], dr = closest_pair_dist_solution(P[mid:], n-mid)
    P = merge(P[:mid], P[mid:])

    d = min(dl, dr)

    Pm = []
    new_mid = 0
    for i in range(n):
        if abs(P[i][0] - mid_x) < d:
            Pm.append(P[i])

    ds = strip_closet_solution(Pm, d)
    return P, ds


n = int(input("점의 전체 개수 : "))
p = []
for i in range(n):
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    p.append((x, y))

p.sort(key = lambda point: point[0])
print(p)
print(closest_pair(p)[1])
print(closest_pair_dist_solution(p, len(p))[1])
