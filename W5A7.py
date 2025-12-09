def calc(num1,num2,operat):
    if operat == '+':
        res = num1 + num2
    elif operat == '-':
        res = num1 - num2
    elif operat == '*':
        res = num1 * num2
    elif operat == '/':
        res = num1 / num2
    return "{:.2f}".format(res)
s = input()
fnum = ""
snum = ""
lostr = s.split()
num1 = float(lostr[0])
num2 = float(lostr[2])
operat = lostr[1]
print(calc(num1,num2,operat))

        
