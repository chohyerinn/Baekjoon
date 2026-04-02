T = int(input())

for _ in range(T):
    n = int(input())
    clothes = {}

    for _ in range(n):
        name, kind = input().split()
        clothes[kind] = clothes.get(kind, 0) + 1

    result = 1 
    for count in clothes.values():
        result *= (count + 1)

    print(result - 1)