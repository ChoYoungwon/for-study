# 분할 정복을 사용한 0-1 배낭 문제 해결 함수
def kn_dc(W, wt, val, n):
    # 기저 조건: 배낭의 용량이 0이거나, 더 이상 고려할 항목이 없는 경우
    if n == 0 or W == 0:
        return 0
    # 현재 항목의 무게가 배낭의 용량을 초과하는 경우, 이 항목을 배낭에 넣을 수 없으므로 다음 항목을 고려
    if (wt[n-1] > W):
        return kn_dc(W, wt, val, n-1)
    else:
        # 현재 항목을 배낭에 넣지 않는 경우와 넣는 경우를 모두 고려하여, 가치가 더 높은 경우를 선택
        valwithout = kn_dc(W, wt, val, n-1)
        valwith = val[n-1] + kn_dc(W-wt[n-1], wt, val, n-1)
        return max(valwith, valwithout)

# 테뷸레이션을 사용한 0-1 배낭 문제 해결 함수
def kn_dp(W, wt, val, n):
    A = [[0 for _ in range(W+1)] for _ in range(n+1)]

    # 각 항목과 각 가능한 배낭의 용량에 대해 최대 가치를 계산
    for i in range(1, (n+1)):
        for w in range(1, (W+1)):
            # 현재 항목의 무게가 배낭의 용량을 초과하는 경우, 이 항목을 배낭에 넣을 수 없으므로 이전 항목의 가치를 사용
            if wt[i-1] > w:
                A[i][w] = A[i-1][w]
            else:
                # 현재 항목을 배낭에 넣는 경우와 넣지 않는 경우를 모두 고려하여, 가치가 더 높은 경우를 선택
                valwith = val[i-1]+A[i-1][w-wt[i-1]]
                valwithout = A[i-1][w]
                A[i][w] = max(valwith, valwithout)
    # 배낭의 최대 용량에 대한 최대 가치를 반환
    return A[n][W]

# 메모이제이션을 사용한 0-1 배낭 문제 해결 함수
def kn_dp_mem(W, wt, val, n):
    if mem[n][W] == 0:
        # 기저 조건: 배낭의 용량이 0이거나, 더 이상 고려할 항목이 없는 경우
        if n == 0 or W == 0:
            return 0
        # 현재 항목의 무게가 배낭의 용량을 초과하는 경우, 이 항목을 배낭에 넣을 수 없으므로 다음 항목을 고려
        if (wt[n-1] > W):
            mem[n][W] = kn_dp_mem(W, wt, val, n-1)
        else:
            # 현재 항목을 배낭에 넣지 않는 경우와 넣는 경우를 모두 고려하여, 가치가 더 높은 경우를 선택
            valwithout = kn_dp_mem(W, wt, val, n-1)
            valwith = val[n-1] + kn_dp_mem(W-wt[n-1], wt, val, n-1)
            mem[n][W] = max(valwithout, valwith)
    return mem[n][W]

# 억지 기법을 사용한 0-1 배낭 문제 해결 함수
def knp(W, wt, val, n):
    max_value = 0
    # 가능한 모든 항목 조합을 고려
    for i in range(2**n+1):
        value = 0
        weight = 0
        for j in range(n):
            # i의 j번째 비트가 1인 경우, 해당 항목을 배낭에 넣는다.
            if (i >> j) & 1:
                value += val[j]
                weight += wt[j]
        # 배낭의 용량을 초과하지 않는 경우, 최대 가치를 업데이트
        if weight <= W and value > max_value:
            max_value = value
    return max_value


val = [60, 100, 190, 120, 200, 150, 130, 90, 50, 210]
wt = [2, 5, 8, 4, 7, 6, 5, 3, 1, 9]
W = 22
n = len(val)
mem = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
print("0-1배낭문제(분할 정복): ", kn_dc(W, wt, val, n))
print("0-1배낭문제(테뷸레이션): ", kn_dp(W, wt, val, n))
print("0-1배낭문제(메모이제이션): ", kn_dp_mem(W, wt, val, n))
print("0-1배낭문제(억지기법): ", knp(W, wt, val, n))