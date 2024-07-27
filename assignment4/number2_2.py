import random

def insertion_sort(A):
    # 기본 케이스: 리스트에 원소가 1개 또는 없을 경우, 이미 정렬된 상태
    if len(A) <= 1:
        return A

    # 재귀 케이스: 리스트의 첫 n-1개 원소를 정렬
    A[:-1] = insertion_sort(A[:-1])

    # 마지막 원소를 정렬된 리스트 부분에 삽입
    j = len(A)-2  # 두 번째로 마지막 원소부터 시작
    key = A[-1]  # 삽입할 마지막 원소

    # key값의 위치 확인
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1

    # key를 올바른 위치에 삽입
    A[j+1] = key
    print(A)
    # 정렬된 리스트를 반환
    return A

print("리스트의 길이 : ")
num = int(input())  # 리스트의 길이를 입력
ls = list(range(1, num + 1))  # 1부터 num까지의 정수로 리스트를 생성
random.shuffle(ls)  # 리스트를 무작위로 섞는다
print("정렬 이전 : ", ls)  # 정렬 전의 리스트를 출력
print("정렬 후 : ", insertion_sort(ls))  # 정렬 후의 리스트를 출력
