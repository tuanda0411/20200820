a, b = map(int, input().split())
for b in range(b): 
    if a % 10 == 0:
        a = a / 10
    else:
        a -= 1
print(int(a))
#1000000000 