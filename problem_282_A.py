number_of_expressions = int(input())
count = 0
for _ in range(number_of_expressions):
    expression = input()
    if "++" in expression:
        count += 1
    elif "--" in expression:
        count -= 1
    else:
        pass
print(count)