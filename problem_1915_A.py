def oddOneOutSimple():
    t = int(input())
    for i in range(t):
        a,  b, c = map(int, input().split())
        if a == b:
            return c
        elif a == c:
            return b
        else:
            return a

def oddOneOutBitmask():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        # Har bir raqamni maskga qo‘shamiz
        mask = (1 << a) | (1 << b) | (1 << c)
        
        # Chastota sanash
        cnt = [0] * 10
        for x in (a, b, c):
            cnt[x] += 1
        
        # Faqat bir marta uchraganini chiqaramiz
        for x in range(10):
            if (mask >> x) & 1 and cnt[x] == 1:
                return x
                

if __name__ == "__main__":
    print(oddOneOutBitmask())
