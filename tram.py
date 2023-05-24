stops=int(input())
bign=0
operation = 0
for i in range(stops):
    a, b = map(int, input().split())
    operation += b - a
    bign = max(bign, operation)     

print(bign)


