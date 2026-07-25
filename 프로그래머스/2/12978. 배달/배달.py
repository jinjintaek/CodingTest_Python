import heapq
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    INF = float('inf')
    distance = [INF] * (N + 1)
    distance[1] = 0
    
    q = []
    heapq.heappush(q, (0,1))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
            
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost,next_node))
                
    for i in distance[1:]:
        if i <= K:
            answer += 1
        
    
    return answer