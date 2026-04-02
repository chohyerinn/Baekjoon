T = int(input())

for _ in range(T):
    s = input()
    count = 0

    for ch in s:
        if ch == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            print("NO")
            break
    else:
        if count == 0:
            print("YES")
        else:
            print("NO")