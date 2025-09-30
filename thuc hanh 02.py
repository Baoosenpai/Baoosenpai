#W2A3
a= int(input ('nhập số nguyên: '))
b= int(input ('nhập số nguyên: '))
print("tổng là:", a + b)
print("hiệu là:", a - b)
print("tích là:", a * b)
print("thương là:", a / b)     
print("thương nguyên là:", a // b)   
print("phần dư là:", a % b)     

#W2A4
a= float(input(' điểm hệ số 1 thứ nhất :'))
b= float(input(' điểm hệ số 1 thứ hai :'))
c= float(input(' điểm hệ số 1 thứ ba :'))
d= float(input('điểm hệ số 2 thứ nhất :'))
e= float(input("điểm hệ số 2 thứ hai :"))
f= float(input("điểm hệ số 3 thứ nhất:"))
print ('điểm trung bình môn ', (((a+b+c)+(e+d)*2+(f *3))/10)) 

#W2A5
a= int(input ('nhập số nguyên: '))
b= int(input ('nhập số nguyên: '))
print('a^b =', a**b)

#W2A6
a = input("Nhập một ký tự chữ cái thường ('a'...'z'): ")
print("Mã Unicode của ký tự:", ord(a))
ainhoa  = a.upper()
print("Ký tự hoa tương ứng:", ainhoa)
  

#W2A7
A = (13 ** 2) * 3
B = 13**2*3 + 5 
 
#W2A8
C = float(input('độ C='))
F = (9 * C) / 5 + 32
Fed = round(F,2)
print('độ F =', Fed)

#w2A9
a = float(input('Nhập số tiền gốc: '))

print('giá gốc của điện thoai:', a )
print('số tiền bỏ ra để nhận điện thoại là :', a+ a*(0.3+0.1)) 
 
#W2A11
a = int(input(' giờ :'))
b = int(input(' phút :'))
if a < 0 or b < 0 or b >= 60:
     print("Giờ hoặc phút không hợp lệ!")
else:
     print ('thời gian là :', a,'h',b,'m')
     print('thời gian theo số giây là :', (a*3600)+(b*60))
#w2A12
