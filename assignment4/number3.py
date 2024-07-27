import random

# 리스트를 생성하하는 함수
def make_list():
    print("숫자의 개수(1 제외하고 입력) : ")
    n = int(input())
    ls = list(range(1, n + 1))  # 1부터 n까지의 숫자로 리스트를 생성
    num = random.randint(1, n)  # 리스트에서 제거할 숫자를 무작위로 선택
    ls.remove(num)  # 선택한 숫자를 리스트에서 제거
    return ls  # 숫자가 제거된 리스트를 반환

# 리스트에서 빠진 숫자를 찾는 함수
def find_number(ls):
    if ls[0] != 1:  # 리스트의 첫 번째 숫자가 1이 아닌 경우, 빠진 숫자 : 1
        print(ls)
        print("빠진 숫자 : ", 1)
        return
    # 리스트의 마지막 숫자가 리스트의 길이와 같은 경우, 빠진 숫자는 마지막 숫자+1
    elif ls[-1] == len(ls):
        print(ls)
        print("빠진 숫자 : ", ls[-1] + 1)
        return
    else:
        # 이진 탐색을 사용하여 빠진 숫자를 탐색
        low = 0
        high = len(ls) - 1
        while low <= high:
            mid = low + (high - low) // 2
            # 중간값이 인덱스+1과 같다면, 빠진 숫자는 오른쪽
            if ls[mid] - mid == 1:
                low = mid + 1 # 중간값이 인덱스+1과 다르다면, 빠진 숫자는 왼쪽

            elif ls[mid] - mid == 2:
                high = mid - 1
            print(low, high)
        print(ls)
        print("빠진 숫자 : ", ls[low] - 1)  # 빠진 숫자를 출력

try:
    find_number(make_list())  # 빠진 숫자를 찾는 함수 실행
except IndexError:  # 사용자가 1을 입력한 경우, 예외를 처리하고 다시 입력을 요청
    print("1을 입력하셨습니다. \n")
    print("다시 입력해주세요")
    find_number(make_list())
