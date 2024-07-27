import random
def isSafe(g, v, c, color):
    for i in range(len(g)):
        if g[v][i] == 1 and color[i] == c:
            return False
    return True

def DFS_graph_coloring(graph, k, v, color):
    if v == len(graph):
        return True

    for c in range(1, k+1):
        if isSafe(graph, v, c, color):
            color[v] = c
            if DFS_graph_coloring(graph, k, v+1, color):
                return True
            color[v] = 0
    return False

def graphColouring(graph, k, states):
    color = [0]*len(graph)
    ret = DFS_graph_coloring(graph, k, 0, color)
    if ret:
        for i in range(len(graph)):
            print("%3s = "%states[i], color_name[color[i]])
        return True
    else:
        print(f"{k}개로 그래프를 색칠할 수 없음!\n")
        return False

def make_graph(n):
    # 0으로 2차원 리스트를 초기화
    ls = [[0 for _ in range(n)] for _ in range(n)]

    # 무작위 인접행렬 제작
    for i in range(n):
        for j in range(n):
            ls[i][j] = random.randint(0, 1)

    for i in range(n):
        for j in range(n):
            if j > i:
                ls[j][i] = ls[i][j]
            if j == i:
                ls[j][i] = 0
        print(ls[i])
    return ls

states = ['NT', 'WA', 'Q', 'SA', 'NSW', 'V']
color_name= ["none", "빨강", "초록", "파랑", "노랑", "보라"]

g = make_graph(len(states))

num = 2
while num:
    if graphColouring(g, num, states):
        print(f'색칠 가능한 최소 색상 개수 : ', num)
        break
    num+=1


