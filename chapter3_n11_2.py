import random                               # 개선된 알고리즘

ex = {1: 'A', 2: 'B', 3: 'D', 4: 'E'}       # A와 B의 개수의 적절한 조절을 위해 알파벳 4개로 한정
ls = []
n = random.randint(2, 10)
for i in range(n):                          # 리스트를 랜덤 알파벳으로 설정
    ls.append(random.randint(1, 4))

count = 0
A_count = 0                                 # 탐색하며, A의 개수를 추가 및 유지하는 변수
for i in range(len(ls)):                    # 문자열 끝까지 탐색
    if ls[i] == 1:                          # A를 찾은 경우 A_count 1증가
        A_count += 1
    elif ls[i] == 2:                        # B를 찾은 경우 count를 B 이전의 A의 개수 만큼 더해준다.
        count += A_count

for i in range(n):                          # 번호를 해당 알파벳과 매칭시켜 문자열을 출력
    ls[i] = ex[ls[i]]
new_ls = "".join(ls)
print(new_ls)
print(count)                                # 부분 문자열의 개수를 출력
