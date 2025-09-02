n, k = map(int, input().split())
nums = list(map(int, input().split()))
kerakli_son = nums[k - 1]
count = 0
for i in range(len(nums)):
    if nums[i] >= kerakli_son and nums[i] != 0:
        count += 1
print(count)
    