#1 - Tổng các số từ 1 đến n
n = int(input())
tong = 0
for i in range(1, n + 1):
    tong += i
print(tong)

#2 - Nhập số nguyên dương + kiểm tra số nguyên tố
while True:
    try:
        n = int(input("nhập số nguyên dương: "))
        if n >= 0:
            print("bạn đã nhập số nguyên dương", n)
            break
        else:
            print("số bạn nhập không phải số nguyên dương")
    except ValueError:
        print("số bạn nhập không phải số nguyên dương")

if n <= 1:
    print(n, "không phải số nguyên tố")
else:
    la_snt = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_snt = False
            break
    if la_snt:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải số nguyên tố")

#3 - Tính giai thừa
n = int(input("số cần tính giai thừa: "))
gt = 1
for i in range(1, n + 1):
    gt *= i
print("giai thừa của", n, "là", gt)

#4 - Đếm số chữ số (xử lý số âm và 0)
n = int(input())
m = abs(n)
if m == 0:
    print(1)
else:
    dem = 0
    while m > 0:
        dem += 1
        m = m // 10
    print(dem)

#5 - Tìm 42 trong mảng
n = int(input("Nhập số nguyên dương n: "))
arr = list(map(int, input(f"Nhập {n} số nguyên: ").split()))

if 42 in arr:
    print("I've found the meaning of life!")
else:
    print("It's a joke!")

#6 - Tổng các số nguyên tố trong đoạn [a, b]
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if a > b:
    a, b = b, a

def songuyento(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

tong = 0
for i in range(a, b + 1):
    if songuyento(i):
        tong += i
print(f"Tổng các số nguyên tố trong đoạn [{a}, {b}] là: {tong}")

#7 - Ước số nguyên tố lớn nhất của n
n = int(input("nhập số n: "))
def snt(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

uoc_lon_nhat = 1
for i in range(n, 1, -1):
    if n % i == 0 and snt(i):
        uoc_lon_nhat = i
        break
print("Ước số nguyên tố lớn nhất của", n, "là:", uoc_lon_nhat)

#8 - Tìm số đối xứng bằng cách cộng số đảo ngược
n = int(input("nhập số n: "))
def so_doi_xung(x):
    s = str(x)
    return s == s[::-1]

def so_dao_nguoc(x):
    return int(str(x)[::-1])

dem = 0
while not so_doi_xung(n):
    n = n + so_dao_nguoc(n)
    dem += 1
print("số đối xứng:", n)
print("số lần cộng:", dem)

#9 - Các bình phương hoàn hảo có chữ số khác nhau ≤ n
def perfect_squares_distinct(n):
    res = []
    i = 1
    while i * i <= n:
        sq = i * i
        s = str(sq)
        if len(set(s)) == len(s):
            res.append(s)
        i += 1
    return res

try:
    n = int(input().strip())
    if n <= 0:
        print("no number")
    else:
        ans = perfect_squares_distinct(n)
        if ans:
            print(" ".join(ans))
        else:
            print("no number")
except:
    print("no number")

#10 - Số có chuỗi Collatz dài nhất từ 1 đến n
n = int(input())
max_len = 0
num = 1

def collatz_length(x):
    length = 1
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        length += 1
    return length

for i in range(1, n + 1):
    l = collatz_length(i)
    if l > max_len or (l == max_len and i < num):
        max_len = l
        num = i
print(num, max_len)

#11 - Đếm ước chẵn của n
import math

n = int(input())
count = 0
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        if i % 2 == 0:
            count += 1
        if i != n // i and (n // i) % 2 == 0:
            count += 1
print(count)

#12 - Tiền gửi ngân hàng lãi suất 0.7%/tháng
X, N = map(int, input().split())
rate = 0.007
amount = X
for _ in range(N):
    amount += amount * rate
print(int(amount))

#13 - Số thân thiết (amicable numbers)
def so_than_thiet(n):
    s = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s

a, b = map(int, input().split())
if a != b and so_than_thiet(a) == b and so_than_thiet(b) == a:
    print("true")
else:
    print("false")

#14 - Ước chung lớn nhất (GCD)
import math

a, b = map(int, input().split())
print(math.gcd(a, b))

#15 - Giải bài toán gà và chó (2 đầu + 4 chân)
T, C = map(int, input().split())
if C % 2 != 0:
    print("invalid")
else:
    c = (C - 2 * T) // 2
    g = T - c
    if c >= 0 and g >= 0 and 2 * g + 4 * c == C:
        print(g, c)
    else:
        print("invalid")

#16 - In số chẵn chia hết cho 3 từ 0 đến 99
for i in range(0, 100, 2):
    if i % 3 == 0:
        print(i)

#17 - Bảng cửu chương
a = int(input())
for i in range(1, 11):
    print(a, "x", i, "=", a * i)

#18 - In các ước chung của a và b
a, b = map(int, input().split())
limit = min(a, b)
for i in range(1, limit + 1):
    if a % i == 0 and b % i == 0:
        print(i, end=" ")

#19 - In các số chẵn từ 0 đến n
n = int(input())
for i in range(0, n + 1):
    if i % 2 == 0:
        print(i)

#20 - Kiểm tra n có phải là lũy thừa của 2
n = int(input())
if n <= 0:
    print("NO")
else:
    while n % 2 == 0:
        n //= 2
    print("YES" if n == 1 else "NO")

#21 - Tổng các chữ số trong chuỗi
n = input()
s = 0
for c in n:
    if c.isdigit():
        s += int(c)
print(s)

#22 - Đếm số chữ số chẵn/lẻ trong chuỗi
n = input().strip()
even = 0
odd = 0
for c in n:
    if c.isdigit():
        if int(c) % 2 == 0:
            even += 1
        else:
            odd += 1
print(even, odd)

#23 - Tìm k lớn nhất sao cho 1 + 2 + ... + k < n
n = int(input())
s = 0
k = 0
while True:
    if s + (k + 1) < n:
        k += 1
        s += k
    else:
        break
print(k)

#24 - Tìm k nhỏ nhất sao cho 1 + 1/2 + ... + 1/k > n
n = float(input())
s = 0.0
k = 0
while s <= n:
    k += 1
    s += 1 / k
print(k)

#25 - Tìm max và min trong dãy số nhập đến -1
nums = []
while True:
    x = int(input())
    if x == -1:
        break
    nums.append(x)

if len(nums) == 0:
    print("No numbers entered")
else:
    print(max(nums), min(nums))

#26 - Số Fibonacci lớn nhất ≤ a
a = int(input())
f1, f2 = 1, 1
if a < 1:
    print(0)
else:
    while f2 <= a:
        f1, f2 = f2, f1 + f2
    print(f1)

#27 - Đếm số từ trong chuỗi
s = input().strip()
count = 0
in_word = False
for c in s:
    if c != " " and not in_word:
        count += 1
        in_word = True
    elif c == " ":
        in_word = False
print(count)

#28 - In ký tự đầu tiên của chuỗi
s = input().strip()
if len(s) == 0:
    print("")
else:
    print(s[0])

#29 - Tổng 3 số nguyên nhập cách nhau bởi khoảng trắng
chuoi = input("Nhập 3 số nguyên cách nhau bởi khoảng trắng: ")
so_list = chuoi.split()
so_list = [int(x) for x in so_list]
tong = sum(so_list)
print("Tổng 3 số nguyên là:", tong)

#30 - Đếm chữ in hoa, in thường, số trong chuỗi
chuoi = input("Nhập vào một chuỗi: ")
dem_in_hoa = 0
dem_in_thuong = 0
dem_so = 0
for ch in chuoi:
    if ch.isupper():
        dem_in_hoa += 1
    elif ch.islower():
        dem_in_thuong += 1
    elif ch.isdigit():
        dem_so += 1
print("Số chữ in hoa:", dem_in_hoa)
print("Số chữ in thường:", dem_in_thuong)
print("Số ký tự số:", dem_so)

#31 - Tổng các chữ số có trong chuỗi (với hiển thị quá trình)
def tinh_tong_cac_ky_tu_so(chuoi):
    tong = 0
    cac_ky_tu_so = []
    for ky_tu in chuoi:
        if ky_tu.isdigit():
            gia_tri_so = int(ky_tu)
            tong += gia_tri_so
            cac_ky_tu_so.append(ky_tu)
    bieu_thuc_tong = " + ".join(cac_ky_tu_so)
    print(f"Các ký tự số được tìm thấy: {', '.join(cac_ky_tu_so)}")
    print(f"Biểu thức tổng: {bieu_thuc_tong}")
    return tong

chuoi_mau = input()
print(f"Chuỗi nhập vào: {chuoi_mau}")
ket_qua = tinh_tong_cac_ky_tu_so(chuoi_mau)
print("---")
print(f"Tổng cuối cùng là: {ket_qua}")

#32 - Kiểm tra mật khẩu mạnh (≥8 ký tự, có hoa/thường/số/ký tự đặc biệt)
def la_mat_khau_manh(chuoi):
    co_hoa = co_thuong = co_so = co_dac_biet = False
    if len(chuoi) < 8:
        return False
    for ch in chuoi:
        if ch.isupper():
            co_hoa = True
        elif ch.islower():
            co_thuong = True
        elif ch.isdigit():
            co_so = True
        elif not ch.isalnum():
            co_dac_biet = True
    return co_hoa and co_thuong and co_so and co_dac_biet

mk = input("Nhập mật khẩu: ")
if la_mat_khau_manh(mk):
    print("Đây là mật khẩu mạnh.")
else:
    print("Mật khẩu chưa đủ mạnh.")

#33 - Định dạng số với dấu chấm mỗi 3 chữ số
so = int(input("Nhập số nguyên: "))
so_dinh_dang = "{:,}".format(so).replace(",", ".")
print("Số sau khi định dạng:", so_dinh_dang)

#34 - Xóa chuỗi b khỏi chuỗi a
a = input("Nhập chuỗi a: ")
b = input("Nhập chuỗi b: ")
a_moi = a.replace(b, "")
print("Chuỗi sau khi xóa:", a_moi)
