def bits(x):
    res = ""
    while x != 0:
        res = str(x%2) + res
        x //= 2
    return res
a,b = map(int,input().split())
x = bits(a)
y = bits(b)
fin = 0
while len(x) < len(y):
    x = '0' + x
while len(y) < len(x):
    y = '0' + y
for i in range(len(x)):
    fin += abs(int(x[i])-int(y[i]))
print(fin)
               
