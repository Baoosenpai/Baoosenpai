def isPrime(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    for i in range(5,int(x**0,5) + 1,6):
        if x % i == 0 or x % (i+2) == 0:
            return False
    return True
n = int(input())
if isPrime(n):
    print("True")
else:
    print("False")
