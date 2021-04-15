n = int(input())
i = int(0)
j = int(0)
nums = []
while n > i:
    var = int(input())
    nums.append(var)
    i = i + 1
while n > j:
    if nums[j-1] > 0 and nums[j] > 0:
        print("YES")
        break
    elif nums[j-1] < 0 and nums[j] < 0:
        print("YES")
        break
    else:
        print("NO")
    j = j + 1