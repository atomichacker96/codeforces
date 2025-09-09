import math

def fine():
    n = int(input())
    min_01 = math.inf
    min_10 = math.inf
    min_11 = math.inf

    for _ in range(n):
        a, b = input().split()
        a = int(a)
        if b == '01':
            min_01 = min(min_01, a)
        elif b == '10':
            min_10 = min(min_10, a)
        elif b == '11':
            min_11 = min(min_11, a)

    ans = min(min_11, min_01 + min_10)
    return ans if ans < math.inf else -1

def main():
    t = int(input())
    for _ in range(t):
        print(fine())

if __name__ == "__main__":
    main()
