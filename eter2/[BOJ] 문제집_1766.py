import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
answer = []
graph = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]
q = []

for i in range(m):
    first, second = map(int, sys.stdin.readline().split())
    graph[first].append(second)
    degree[second] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(q, i)
        
while q:
    tmp = heapq.heappop(q)
    answer.append(tmp)
    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(q, i)

print(" ".join(map(str, answer)))
