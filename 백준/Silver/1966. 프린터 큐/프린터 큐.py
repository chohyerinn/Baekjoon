from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue = deque()
    for i in range(n):
        queue.append((priorities[i], i))   

    count = 0

    while queue:
        now = queue.popleft()

        if any(now[0] < x[0] for x in queue):
            queue.append(now)
        else:
            count += 1
            if now[1] == m:
                print(count)
                break