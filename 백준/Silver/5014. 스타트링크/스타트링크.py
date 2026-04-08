from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [-1] * (F + 1)
queue = deque()

queue.append(S)
visited[S] = 0

while queue:
    now = queue.popleft()

    if now == G:
        print(visited[now])
        break

    up = now + U
    down = now - D

    if up <= F and visited[up] == -1:
        visited[up] = visited[now] + 1
        queue.append(up)

    if down >= 1 and visited[down] == -1:
        visited[down] = visited[now] + 1
        queue.append(down)
else:
    print("use the stairs")