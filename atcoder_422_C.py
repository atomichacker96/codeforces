
def solve(a, b, c):
    return min(a, c, (a + b + c) // 3)

def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        print(solve(a, b, c))
    pass

if __name__ == "__main__":
    main()
