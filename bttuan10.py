#1 - Chia 2 số, in 2 chữ số thập phân
def chia(x, y):
    try:
        return f"{x / y:.2f}"
    except:
        print("Loi chia khong")

a, b = map(int, input().split())
print(chia(a, b))

#2 - Truy cập phần tử theo index, bắt lỗi IndexError
def indx(a, k):
    try:
        return a[k]
    except IndexError:
        print("index nam ngoai list")

n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
print(indx(a, n))

#3 - Kiểm tra số Happy (liên tục bình phương tổng chữ số)
def Happynumbers(k):
    a = 100  # giá trị ban đầu lớn hơn 10
    while a >= 10:
        s = 0
        while k > 0:
            tmp = k % 10
            s += tmp ** 2
            k = k // 10
        a = s
        k = s
    if a == 1:
        return "Yes"
    else:
        return "No"

try:
    n = int(input())
    print(Happynumbers(n))
except ValueError:
    print("n must be number")

#4 - Cộng 2 số, bắt lỗi nhập không phải số + finally
try:
    a, b = map(int, input().split())
    print(a + b)
except ValueError:
    print("a and b must be number")
finally:
    print("Ket thuc chuong trinh")

#5 - Chuyển các phần tử chuỗi thành int nếu được, in thông báo nếu không
a = input().split()
for i in range(len(a)):
    try:
        a[i] = int(a[i])
    except ValueError:
        print(f"{a[i]} khong phai so")
        # continue không cần vì vòng lặp vẫn chạy tiếp

#6 - Căn bậc 2, bắt lỗi số âm
from math import sqrt

try:
    a = int(input())
    print(sqrt(a))
except ValueError:
    print("So Am")

#7 - Tính năm tương lai (tuổi), bắt lỗi số âm
try:
    n = int(input())
    if n < 0:
        raise ValueError("So tuoi phai duong")
    else:
        print(2025 + n)
except ValueError as e:
    print("Invalid Yearolds:", e)

#8 - Kiểm tra đuôi file .txt hoặc .zip (không phân biệt hoa/thường)
namefile = input()
typefi = namefile[-4:].lower()  # lấy 4 ký tự cuối và chuyển thường

try:
    if typefi in [".txt", ".zip"]:
        print("Doc file thanh cong")
    else:
        raise ValueError("File khong hop le")
except ValueError as e:
    print(e)

#9 - Chuyển chuỗi thành int, bắt lỗi nếu có dấu chấm hoặc không phải số
try:
    n = input()
    x = int(n)
    if '.' in n:
        raise Exception("Chuoi khong hop le")
    else:
        print(x)
except ValueError:
    print("Chuoi khong hop le")
except Exception as e:
    print(e)

#10 - Nhập mảng, kiểm tra trùng phần tử (dùng dict), bắt lỗi nhập không phải số
try:
    n = int(input())
    b = {}
    for i in range(n):
        x = int(input())
        if x in b:
            raise Exception("Mang khong hop le")
        else:
            b[x] = 1
except ValueError:
    print("n and ptu must be number")
except Exception as e:
    print(e)

#11 - Kiểm tra regex cơ bản hợp lệ (không có * hoặc + ở đầu, không lặp toán tử, escape đúng)
def is_valid_regex(s):
    n = len(s)
    i = 0
    prev_repeat = False

    while i < n:
        if s[i] == '\\':
            if i + 1 >= n:
                return False
            prev_repeat = False
            i += 2
        elif s[i] in ['*', '+']:
            if i == 0 or prev_repeat:
                return False
            prev_repeat = True
            i += 1
        else:
            prev_repeat = False
            i += 1
    return True

t = int(input())
for _ in range(t):
    s = input().strip()
    try:
        if not is_valid_regex(s):
            raise Exception("Invalid")
        else:
            print("Valid")
    except Exception as e:
        print(e)