n = int(input())
i = int(0)
j = int(0)
cnt = int(0)
nums = []
while n > i:
    var = int(input())
    nums.append(var)
    i = i + 1
while n > j:
    if nums[j - 1] < nums[j]:
        cnt = cnt + 1
    j = j + 1
print(cnt)