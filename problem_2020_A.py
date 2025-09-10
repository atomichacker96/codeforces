
def solve(n, k):
    res = 0
    while n > 0:
        res += n % k
        n //= k
    return res

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
    
