import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()

mean = round(sum(nums) / n)

median = nums[n // 2]

from collections import Counter
cnt = Counter(nums)

max_freq = max(cnt.values())
modes = []

for num in cnt:
    if cnt[num] == max_freq:
        modes.append(num)

modes.sort()

if len(modes) > 1:
    mode = modes[1]   
else:
    mode = modes[0]

range_val = nums[-1] - nums[0]

print(mean)
print(median)
print(mode)
print(range_val)