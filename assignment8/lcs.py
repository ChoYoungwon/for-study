import copy

# 동적 프로그래밍을 사용한 최장 공통 부분열(LCS) 문제 해결 함수
def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    # LCS 테이블 초기화
    L = [[None]*(n+1) for _ in range(m+1)]

    # LCS 테이블 채우기
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:  # 첫 번째 행과 열은 0으로 채운다
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:  # 두 문자가 같으면 대각선 위의 값에 1을 더한다
                L[i][j] = L[i-1][j-1]+1
            else:  # 두 문자가 다르면 왼쪽과 위쪽의 값 중 큰 값을 선택
                L[i][j] = max(L[i-1][j], L[i][j-1])
    # 전역 변수 LW에 L 테이블을 복사
    global LW
    LW = copy.deepcopy(L)
    # 최종적으로 계산된 LCS의 길이를 반환
    return L[m][n]

# 메모이제이션을 사용한 LCS 문제 해결 함수
def lcs_dp_mem(X, Y, m, n):
    if mem[m][n] is None:
        if m == 0 or n == 0:  # 첫 번째 행과 열은 0으로 채운다.
            return 0
        elif X[m-1] == Y[n-1]:  # 두 문자가 같은 경우
            mem[m][n] = 1+lcs_dp_mem(X, Y, m-1, n-1)
        else:  # 두 문자가 다른 경우
            mem[m][n] = max(lcs_dp_mem(X, Y, m-1, n), lcs_dp_mem(X, Y, m, n-1))
    return mem[m][n]

# LCS 테이블을 사용하여 실제 LCS를 추적하는 함수
def lcs_dp_traceback(X, Y, L):
    lcs = ""  # LCS를 저장할 문자열
    i = len(X)
    j = len(Y)
    # LCS 테이블을 거꾸로 추적
    while i > 0 and j > 0:
        v = L[i][j]
        if v > L[i-1][j-1] and v > L[i-1][j] and v > L[i-1][j-1]:  # 대각선 위의 값이 가장 큰 경우
            i -= 1
            j -= 1
            lcs = X[i] + lcs  # LCS에 현재 문자를 추가
        elif v == L[i][j-1] and v > L[i-1][j]:  # 왼쪽의 값이 가장 큰 경우
            j -= 1
        else:  # 위쪽의 값이 가장 큰 경우
            i -= 1
    return lcs  # 계산된 LCS를 반환


X = "DATA STRUCTURE"
Y = "PYTHON ALGORITHM"
Z = "DELTA AIRPLANE"
m = len(X)
n = len(Y)
k = len(Z)
LW = [[None]*(n+1) for _ in range(m+1)]
mem = [[None]*(n+1) for _ in range(m+1)]

print("X = ", X)
print("Y = ", Y)
print("Z = ", Z)
print("LCS(테뷸레이션) : ", lcs_dp(X, Y))
print("LCS(메모이제이션) : ", lcs_dp_mem(X, Y, m, n))
print("LCS : ", lcs_dp_traceback(X, Y, LW))

print("LCS(테뷸레이션) : ", lcs_dp(X, Z))
mem = [[None]*(n+1) for _ in range(m+1)]
print("LCS(메모이제이션) : ", lcs_dp_mem(X, Z, m, k))
print("LCS : ", lcs_dp_traceback(X, Z, LW))

