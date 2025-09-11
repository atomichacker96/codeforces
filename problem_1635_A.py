# problem_1635_A.py

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        OR = 0
        for e in nums:
            OR |= e
        print(OR)

if __name__ == "__main__":
    main()
