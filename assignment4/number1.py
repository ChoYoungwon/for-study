import queue
# 그래프를 생성하는 함수
def MakeGraph(k=3):
    # 그래프를 저장할 딕셔너리를 생성
    graph = {}
    # 사용자로부터 입력받은 간선의 개수만큼 반복
    for _ in range(k):
        print("두 원소를 입력하세요 : ")
        x, y = map(str, input().split(" "))
        # 입력받은 두 원소를 그래프에 추가
        if x not in graph.keys():
            graph[x] = set([y])
        else:
            graph[x].add(y)
        if y not in graph.keys():
            graph[y] = set([x])
        else:
            graph[y].add(x)
    # 완성된 그래프 반환
    return graph

def bfs(graph):
    result = True
    # 방문한 노드를 저장하는 집합
    visited = set()
    # 그래프의 모든 노드에 대해 반복
    for start in graph:
        # 아직 방문하지 않은 노드라면
        if start not in visited:
            # 큐를 생성하고 시작 노드를 큐에 넣는다.
            que = queue.Queue()
            que.put(start)
            # 시작 노드를 방문한 것으로 표시
            visited.add(start)
            # 큐가 빌 때까지 반복
            while not que.empty():
                # 큐에서 노드를 하나 꺼낸다
                v = que.get()
                print(v, end=' ')
                # 방문하지 않은 이웃 노드를 찾는다
                nbr = graph[v] - visited
                for u in nbr:
                    # 노드를 큐에 넣고 방문한 것으로 표시
                    que.put(u)
                    visited.add(u)
                    # 이웃 노드 중에서
                    for u2 in nbr:
                        # u2와 연결된 노드가 있으면
                        if u2 in graph[u]:
                            # 그래프는 이분 그래프가 아니다.
                            result = False
    return result

print("간선의 개수를 입력하시오 : ")
n = int(input())
new_graph = MakeGraph(n)
new_graph = dict(sorted(new_graph.items()))
print(new_graph)

# 그래프가 이분 그래프인지 확인하고 결과를 출력
if bfs(new_graph):
    print("이분 그래프입니다.")
else:
    print("이분 그래프가 아닙니다.")
