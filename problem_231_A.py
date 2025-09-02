sana = 0
number_of_problems = int(input())
for i in range(number_of_problems):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        sana += 1
print(sana)