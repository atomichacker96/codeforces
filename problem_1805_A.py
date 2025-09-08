def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        xor_all = 0
        for v in arr:
            xor_all ^= v
        
        if n % 2 == 0:  # juft uzunlik
            if xor_all == 0:
                print(0)
            else:
                print(-1)
        else:  # toq uzunlik
            print(xor_all)

if __name__ == "__main__":
    solve()