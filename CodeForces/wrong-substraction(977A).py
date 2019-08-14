line = input().split()
n = int(line[0])
k = int(line[1])

for i in range(k):
    if n % 10 == 0:
        n = n // 10
    else:
        n -= 1
        
print(n)