weight = int(input())

def watermelon(weight):
    return "YES" if (weight % 2 == 0 and weight >= 4) else "NO"

print(watermelon(weight))