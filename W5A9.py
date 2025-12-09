def calc(x):
    res = 0
    while x != 0:
        res += x%10
        x //= 10
    return res
n = int(input())
print(calc(n))
