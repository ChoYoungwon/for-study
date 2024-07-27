import random

ex = {1: 'A', 2: 'B', 3: 'D', 4: 'E'}       # A와 B의 개수의 적절한 조절을 위해 알파벳 4개로 한정
ls = []
n = random.randint(2, 10)
for i in range(n):                          # 리스트를 랜덤 알파벳으로 설정
    ls.append(random.randint(1, 4))

count = 0
for i in range(len(ls)):            # 문자열의 끝까지 탐색
    if ls[i] == 1:                  # A를 탐색한 경우
        k = i
        while k < len(ls):          # 문자열의 끝까지 B를 탐색
            if ls[k] == 2:          # B를 찾은 경우 count 1증가
                count += 1
            k += 1

for i in range(n):                  # 번호를 해당 알파벳과 매칭시켜 문자열을 출력
    ls[i] = ex[ls[i]]
new_ls = "".join(ls)
print(new_ls)
print(count)                        # 부분 문자열의 개수를 출력
