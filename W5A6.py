def calc(x):
    if x < 0:
        print("no value")
    else:
        res = 1
        while x != 1:
            res *= x
            x -= 1
        print(res)
n = int(input())
calc(n)
