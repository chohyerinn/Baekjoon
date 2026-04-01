T = int(input())

for _ in range(T):
    s = input()
    count = 0
    total = 0
    
    for ch in s:
        if ch == 'O':
            count += 1
            total += count
        else:
            count = 0
    
    print(total)