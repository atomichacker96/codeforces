
def solve(nums):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j] == '.':
                continue
            sana = 0
            if 0 < i < len(nums):
                if nums[i-1][j] == '#':
                    sana += 1
                else:
                    pass
            else:
                pass

            if i < len(nums) - 1:
                if nums[i+1][j] == '#':
                    sana += 1
                else:
                    pass  # oq
            else:
                pass  # past yo'q
            
            if 0 < j < len(nums[0]):
                if nums[i][j-1] == '#':
                    sana += 1
                else:
                    pass  # chap yo'q
            else:
                pass  # chap yo'q

            if j < len(nums[0]) - 1:
                if nums[i][j+1] == '#':
                    sana += 1
                else:
                    pass  # o'ng yo'q
            
            if sana == 1 or sana == 3:
                return 'No'
            else:
                pass
    return 'Yes'
    
def main():
    n, m = map(int, input().split())
    nums = [input().strip() for _ in range(n)]
    print(solve(nums))

if __name__ == "__main__":
    main()
