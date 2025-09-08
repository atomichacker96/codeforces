def f1843C_bitmask(n: int) -> int:
    yigindi = 0
    while n > 0:
        yigindi += n
        n >>= 1   # n //= 2 bilan bir xil, faqat bit amali
    return yigindi

def f1843C(n: int) -> int:
    yigindi = n
    while n > 0:
        asos = n // 2
        yigindi += asos
        n = asos
    return yigindi

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(f1843C(n))

if __name__ == "__main__":
    main()