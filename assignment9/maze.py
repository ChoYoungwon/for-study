import random
import numpy as np
INF = 9999

# 무작위 가중치를 가진 그래프를 생성
def make_graph(x, y, n):
    # INF로 2차원 리스트를 초기화
    ls = [[INF for _ in range(n)] for _ in range(n)]
    # 2차원 리스트를 numpy 배열로 변환
    graph = np.array(ls)
    # 그래프의 간선에 무작위 가중치를 할당
    for i in range(n):
        for j in range(n):
            # 정점이 인접하면 무작위 가중치를 할당
            if ((i % x) != (x-1) and j - i == 1) or (i + x) == j:
                graph[i][j] = random.randint(1, n)
            # 정사각 행렬을 위해 오른쪽의 값을 복사
            if j > i:
                graph[j][i] = graph[i][j]
            # 정점에서 자기 자신으로의 간선의 가중치는 0
            if j == i:
                graph[j][i] = 0
    print(graph)
    return graph

# 이 함수는 최소 거리를 가진 정점을 반환
def getMinVertex(dist, selected):
    minv = -1
    mindist = INF
    # 모든 정점에 대해 반복
    for v in range(len(dist)):
        # 정점이 선택되지 않았고, 그 거리가 최소 거리보다 작으면 최소 정점과 최소 거리를 업데이트한다.
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

# Prim알고리즘.
def MSTPrim(vertex, adj, maze_, nx, ny):
    vsize = len(vertex)
    dist = [INF] * vsize            # 거리 리스트를 INF로 초기화
    dist[0] = 0
    selected = [False] * vsize
    tmp = dict()                    # 각 정점의 부모를 저장하는 빈 딕셔너리를 초기화합니다.

    # 모든 정점에 대해 반복합니다.
    for i in range(vsize):
        u = getMinVertex(dist, selected)         # 최소 거리를 가진 정점을 찾는다.
        selected[u] = True                       # 선택된 정점을 표시.
        print(vertex[u], end=':')
        print(dist)

        # 인접한 정점의 거리를 업데이트
        for v in range(vsize):
            # 정점이 인접하면
            if (adj[u][v] != None):
                # v가 선택되지 않았고, 간선의 가중치가 현재 거리보다 작으면 거리와 v의 부모를 업데이트
                if selected[v] == False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]
                    tmp[v] = u
    print(tmp)
    # 부모 딕셔너리의 모든 정점에 대해 반복합니다.
    for x in tmp:
        # x의 부모를 가져옵니다.
        y = tmp[x]
        # 미로에서 x와 y의 행과 열의 위치를 계산
        x_row = (x // nx)*3+1
        x_col = (x % nx)*3+1

        y_row = (y // nx)*3+1
        y_col = (y % nx)*3+1
        # x와 y의 상대 위치에 따라 미로의 벽을 제거
        if y - x == nx:
            maze_[y_row-1][y_col] = "   "
            maze_[x_row+1][x_col] = "   "
        elif x - y == nx:
            maze_[x_row-1][x_col] = "   "
            maze_[y_row+1][y_col] = "   "
        elif y - x == 1:
            maze_[y_row][y_col-1] = "   "
            maze_[x_row][x_col+1] = "   "
        else:
            maze_[y_row][y_col+1] = "   "
            maze_[x_row][x_col-1] = "   "
    return maze_

# 그래프를 미로로 변환합니다.
def graph_to_array(nx, ny):
    # 그래프를 생성
    graph = make_graph(nx, ny, nx*ny)
    # 벽으로 미로를 초기화합니다.
    maze = [["■" for _ in range(nx*3)] for _ in range(ny*3)]
    # 미로의 셀에서 인덱스에 해당하는 벽을 제거
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if j % 3 == 1 and i % 3 == 1:
                maze[i][j] = "   "

    # 메시지를 출력
    print("\nMST By Prim's Algorithm")
    # 정점 리스트를 생성
    vertex = list(range(len(graph)))
    # 그래프의 최소 신장 트리를 찾아 미로로 변환
    maze_prim = MSTPrim(vertex, graph, maze, nx, ny)
    return maze_prim

# 무작위 미로를 생성하고 파일에 작성
def random_maze(nx, ny):
    # 그래프를 미로로 변환
    maze = graph_to_array(nx, ny)
    # 미로의 시작점과 끝점을 입구와 출구로 설정
    maze[1][0] = "   "
    maze[-2][-1] = "   "
    # 파일을 엽니다.
    file = open('maze.txt', 'w')
    # 미로를 파일에 쓴다.
    for r in maze:
        for c in r:
            file.write(c)
        file.write('\n')
    # 파일을 닫는다.
    file.close()

# 무작위 미로를 생성.
random_maze(13, 10)
