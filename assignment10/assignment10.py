import heapq

# 파일의 주어진 단어를 리스트로 변환
def make_word_table(path):
    f = open(path, "r")
    ls = []
    while True:
        line = f.readline()
        if not line:
            break
        ls.append(line.strip())
    return ls

# 문자의 빈도를 구해 CNT 리스트에 저장 후 반환한다.
def make_count_table():
    cnt = [0 for _ in range(26)]
    ls_ = make_word_table("words.txt")
    for word in ls_:
        for char in word:
            if char.isalpha():
                cnt[ord(char)-ord('a')] += 1
    return cnt

# 허프만 트리
def make_heap_tree(freq, label):
    n = len(freq)
    h=[]
    for i in range(n):
        heapq.heappush(h, (freq[i], label[i]))

    for i in range(1, n):
        e1 = heapq.heappop(h)
        e2 = heapq.heappop(h)
        heapq.heappush(h, (e1[0]+e2[0], e1[1]+e2[1]))
        print(e1, "+", e2)

    print(heapq.heappop(h))

# 이진 트리를 위한 노드 클래스를 정의
class Node:
    def __init__(self, left=None, right=None, alpha='+', frequency=0):
        self.left = left
        self.right = right
        self.alpha = alpha
        self.f = frequency

    # 힙에서 객체의 크기 비교를 위해 작성
    def __lt__(self, other):
        return self.f < other.f

# 루트 노드에서 시작해 깊이 우선으로 탐색, 허프만 코드 계산 함수
def dfs(node, code):
    # 단말 노드 도달시 해당 문자의 코드를 리스트에 저장하고 호출 함수로 돌아간다.
    if node.left is None and node.right is None:
        number = ord(node.alpha)-ord('a')
        hf_code[number]=code
        return

    if node.left is not None:
        code += "0"
        dfs(node.left, code)
        code = code[0:-1]

    if node.right is not None:
        code += "1"
        dfs(node.right, code)

# a-z 까지의 각 알파벳에 대한 허프만 코드
def make_hurffmancode(freq, label):
    n = len(freq)
    h = [(freq[i], Node(alpha=label[i], frequency=freq[i])) for i in range(n)]
    heapq.heapify(h)

    # 허프만 트리를 노드 객체를 이용해 연결 리스트 방식으로 저장
    for i in range(1, n):
        freq1, node1 = heapq.heappop(h)
        freq2, node2 = heapq.heappop(h)

        new_node = Node(left=node1, right=node2, alpha=node1.alpha+node2.alpha, frequency=freq1+freq2)

        heapq.heappush(h, (new_node.f, new_node))

        print((freq1, node1.alpha), "+", (freq2, node2.alpha))
    freq_last, node_last = heapq.heappop(h)
    print((freq_last, node_last.alpha))

    dfs(node_last, "")      # 저장한 노드 객체를 이용해 허프만 코드를 계산한다.
    print()
    print(hf_code)

# 허프만 코드를 사용하여 문자열을 인코딩한다.
def encoder(hf, value):
    bi = ""
    for char in value:
        if char.isalpha():
            bi += hf[ord(char)-ord('a')]
    print(bi)
    return bi

# 허프만 코드를 사용하여 인코딩된 문자열을 디코딩한다..
def decoder(hf, num):
    result = ""
    word = ""
    for char in num:
        word += char
        if word in hf:
            result += chr(hf.index(word)+ord('a'))
            word = ""
    print(result)


label = [chr(ord('a')+k) for k in range(26)]
freq = make_count_table()
hf_code = [None for _ in range(26)]
# label = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# freq = [24, 3, 8, 10, 33, 6, 4, 12]
# make_heap_tree(freq, label)
# print('\n')
make_hurffmancode(freq, label)
decoder(hf_code, encoder(hf_code, "eta"))
decoder(hf_code, encoder(hf_code, "hype"))
decoder(hf_code, encoder(hf_code, "boy"))
decoder(hf_code, encoder(hf_code, "omg"))
