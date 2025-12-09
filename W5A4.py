def isPerfect(x):
    if x < 6:
        return False
    res = 1
    for i in range(2,int(x**0.5)+1,1):
        if x % i == 0:
            if i * i == x:
                res += i
            else:
                res += i + x//i
    if res == x:
        return True
    return False
n = int(input())
if isPerfect(n):
    print("True")
else:
    print("False")
