def f():
    t = int(input())
    for _ in range(t):
        for j in range(3):
            row = input()
            if '?' in row:
                if 'A' in row and 'B' in row:
                    print('C')
                elif 'A' in row and 'C' in row:
                    print('B')
                else:
                    print('A')

def solve():
    FULL = (1 << 3) - 1  # 111 (A,B,C hammasi bor)
    letter = ['A', 'B', 'C']

    t = int(input())
    for _ in range(t):
        grid = [input().strip() for _ in range(3)]
        for row in grid:
            if '?' in row:
                row_mask = 0
                for ch in row:
                    if ch != '?':
                        row_mask |= 1 << (ord(ch) - ord('A'))
                missing_mask = FULL ^ row_mask
                # missing_mask ichida bitta bit bo‘ladi
                missing_letter = letter[(missing_mask.bit_length() - 1)]
                print(missing_letter)
                break


if __name__ == "__main__":
    solve()

