s = input()

for x in range(10):
    total = 0
    
    for i in range(13):
        if s[i] == '*':
            num = x
        else:
            num = int(s[i])
        
        if i % 2 == 0:
            total += num
        else:
            total += num * 3
    
    if total % 10 == 0:
        print(x)
        break