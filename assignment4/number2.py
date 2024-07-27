import random
# 삽입 정렬 함수
def insertion_sort(A):
    # 리스트의 모든 요소에 대해 반복
    for i in range(1, len(A)):
        # 현재 요소를 key로 저장
        key = A[i]
        # 이전 요소의 인덱스를 j로 저장
        j = i-1
        # key보다 이전 요소가 크고, 이전 요소의 인덱스가 0 이상인 동안 반복
        while j >= 0 and key < A[j]:
            # 이전 요소를 한 칸 오른쪽으로 이동
            A[j+1] = A[j]
            # 이전 요소의 인덱스를 하나 감소시킨다
            j -= 1
        # key를 적절한 위치에 삽입
        A[j+1] = key
        print(A)
    # 정렬된 리스트를 반환
    return A

# 리스트의 길이를 입력
print("리스트의 길이 : ")
num = int(input())                      # 1부터 num까지의 숫자로 리스트를 생성.
ls = list(range(1, num + 1))
random.shuffle(ls)                      # 리스트를 무작위로 섞는다(shuffle)
print("정렬 이전 : ", ls)                 # 정렬 전의 리스트를 출력
print("정렬 후 : ", insertion_sort(ls))   # 리스트를 정렬하고 정렬 후의 리스트를 출력
