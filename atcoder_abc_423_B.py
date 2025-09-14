n = int(input())
L = list(map(int, input().split()))

# Chapdan yurish
left = 0
for i in range(n):
    if L[i] == 0:
        left = i + 1
    else:
        break

# O‘ngdan yurish
right = n
for i in range(n-1, -1, -1):
    if L[i] == 0:
        right = i
    else:
        break

ans = max(0, right - left - 1)
print(ans)
