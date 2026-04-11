from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001

visited = [-1] * MAX  

def bfs():
    dq = deque()
    dq.append(N)
    visited[N] = 0

    while dq:
        x = dq.popleft()

        if x == K:
            return visited[K]

        for nx in [x*2, x-1, x+1]:
            if 0 <= nx < MAX and visited[nx] == -1:
                if nx == x*2:
                    visited[nx] = visited[x]     
                    dq.appendleft(nx)              
                else:
                    visited[nx] = visited[x] + 1  
                    dq.append(nx)                 

print(bfs())