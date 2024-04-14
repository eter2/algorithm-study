import heapq, sys

def find_root(v):
    d[v] = 0
    q = []
    heapq.heappush(q, (0, v))
    while q:
        dist, vertex = heapq.heappop(q)
        if d[vertex] < dist: # 저장된 최단 거리가 더 짧으면 다음 간선으로
            continue
        for (nv, nd) in adj[vertex]: # 노드에 연결된 간선 확인
            if nd + dist < d[nv] and not visited[vertex][nv]: # 갱신 O, 최단 경로 X 확인
                d[nv] = nd + dist
                heapq.heappush(q, (nd + dist, nv))
                
def del_root(v):
    q = []
    heapq.heappush(q, (d[v], v))
    while q:
        dist, vertex = heapq.heappop(q)
        if vertex == S: # 시작점이면 종료
            continue
        
        for (bv, bd) in adj2[vertex]: 
            if visited[bv][vertex]: # 이미 최단 경로에 포함된 간선이면 종료
                continue
            
            if d[bv] == d[vertex] - bd: # 최단 경로에 포함되는 간선인 경우
                visited[bv][vertex] = True
                heapq.heappush(q, (d[bv], bv))

INF = int(1e9)
while True:
    N, M = map(int, sys.stdin.readline().split()) # 장소의 수 N, 도로의 수 M
    
    # n과 m이 0이면 종료
    if N == 0 and M == 0:
        break
    
    S, D = map(int, sys.stdin.readline().split()) # 시작점 S, 도착점 D
    
    adj = [[] for _ in range(N)] # 인접리스트
    adj2 = [[] for _ in range(N)] # 역인접리스트
    visited = [[False] * N for _ in range(N)] # 최단 경로 포함 간선 유무 배열
    
    d = [INF] * N # 최단거리 저장
    for i in range(M):
        a, b, c = map(int, sys.stdin.readline().split()) # a에서 b로 가는 길이 c
        adj[a].append((b, c)) # a에서 b로 가는 길이 c
        adj2[b].append((a, c)) # b에서 a로 가는 길이 c
    

    find_root(S) # 시작점부터 끝점까지 최단경로
    del_root(D) # 끝점부터 시작점까지 최단경로에 포함된 간선 갱신
    
    for i in range(N): # 최단경로 포함 간선 제거 후 다시 최단 경로
        d[i] = INF
    find_root(S)
    
    print(d[D] if d[D] != INF else -1) # 정답 출력