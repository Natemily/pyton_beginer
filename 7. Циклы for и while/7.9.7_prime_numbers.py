a, b = int(input()), int(input())
for i in range(a,b + 1):
    s = 0
    for j in range(2, i - 1):
        if i % j == 0:
            s += 1
    if s == 0 and i > 1:
        print(i)