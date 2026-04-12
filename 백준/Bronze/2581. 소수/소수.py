M = int(input())
N = int(input())

findPrime = [True] * (N + 1)
findPrime[0] = findPrime[1] = False

for i in range(2, int(N**0.5) + 1):
    if findPrime[i]:
        for j in range(i*i, N+1, i):
            findPrime[j] = False

result = []
for i in range(max(2, M), N+1):
    if findPrime[i]:
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)