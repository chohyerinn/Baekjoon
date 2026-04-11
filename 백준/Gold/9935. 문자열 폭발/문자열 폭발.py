import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
bomb_last = bomb[-1]
bomb_len = len(bomb)

stack = []

for ch in s:
    stack.append(ch)
    if ch == bomb_last:
        if stack[-bomb_len:] == list(bomb):
            del stack[-bomb_len:]

print(''.join(stack) if stack else 'FRULA')