result = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b == c:
        result = max(result, 10000+a*1000)
    elif a == b:
        result = max(result, 1000+a*100)
    elif b == c:
        result = max(result, 1000+b*100)
    elif a == c:
        result = max(result, 1000+a*100)
    else:
        result = max(result, max(a,b,c)*100)
print(result)