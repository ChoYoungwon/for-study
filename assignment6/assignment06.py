import random
import math

# 두 점 사이의 거리를 반환
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# 억지기법을 사용한 최단 거리 찾기
def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])
            if dist < mindist:
                mindist = dist
    return mindist

# -------------------------------------------------------------------------------------------------------

# 띠 영역을 처리하는 함수(sort 사용)
def strip_closet(P, d):
    n = len(P)
    d_min = d
    P.sort(key = lambda point: point[1])

    for i in range(n):
        j = i + 1
        while j < n and (P[j][1] - P[i][1]) < d_min:
            dij = distance(P[i], P[j])
            if dij < d_min:
                d_min = dij
            j += 1
    return d_min

# 분할 정복 기법을 이용해 거리를 변환 / 시간 복잡도 : (O(n(log n)**2)
def closest_pair_dist(P, n):
    if n <= 3:
        return closest_pair(P)

    mid = n // 2
    mid_x = P[mid][0]

    dl = closest_pair_dist(P[:mid], mid)
    dr = closest_pair_dist(P[mid:], n-mid)
    d = min(dl, dr)

    Pm = []

    for i in range(n):
        if abs(P[i][0] - mid_x) < d:
            Pm.append(P[i])

    ds = strip_closet(Pm, d)
    return ds

# -------------------------------------------------------------------------------------------------------
# 솔루션 코드
# 점이 3개 이하일 때 최소 거리를 구하는 함수(억지 기법)
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

# y기준으로 두 리스트를 한 리스트로 병합 정렬한다 / 시간 복잡도 : O(n)
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
    while i < len(A):                   # 리스트에 남은 원소 정렬
        sorted.append(A[i])
        i += 1
    while j < len(B):                   # 리스트에 남은 원소 정렬
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
    P = merge(P[:mid], P[mid:])                 # merge를 이용해 리스트 p를 y축 기준으로 정렬한다.

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
print(closest_pair(p))
print(closest_pair_dist(p, len(p)))
print(closest_pair_dist_solution(p, len(p))[1])

