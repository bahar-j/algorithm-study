# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque


def solution(n, edge):
    answer = 0

    G = {i: [] for i in range(1, n + 1)}
    dist = [0 for i in range(n + 1)]
    visited = [False for i in range(n + 1)]

    queue = deque()
    queue.appendleft(1)
    visited[1] = True

    for j in range(len(edge)):
        G[edge[j][0]].append(edge[j][1])
        G[edge[j][1]].append(edge[j][0])

    max_path = 0

    while queue:
        start = queue.popleft()

        for k in range(len(G[start])):
            # 방문한 적 없는 자식 노드에 대해 떨어진 거리 update
            if not visited[G[start][k]]:
                tmp = dist[start] + 1
                if dist[G[start][k]] != 0:
                    dist[G[start][k]] = min(dist[G[start][k]], tmp)
                else:
                    dist[G[start][k]] = tmp

                if max_path == dist[G[start][k]]:
                    answer += 1
                elif max_path < dist[G[start][k]]:
                    answer = 1
                    max_path = dist[G[start][k]]

                queue.append(G[start][k])
                # 방문할 노드 목록(queue)에 추가하는 순간 visited를 True로 바꿔줘야함
                visited[G[start][k]] = True

    return answer