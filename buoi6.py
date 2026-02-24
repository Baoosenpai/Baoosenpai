#w6a1
Pythona = list(map(int, input().split()))
mapa = {}
i = 0
while i < len(a):
    if a[i] in mapa:
        a.remove(a[i])
    else:
        mapa[a[i]] = 1
    i += 1
print(a)
#w6a2
Pythona = list(map(int, input().split()))
for i in range(1, len(a)):
    a[i] += a[i-1]
print(a)
#w6a3
Pythona = list(map(int, input().split()))
k = int(input())
k = k % len(a)
for i in range(k):
    t = a[0]
    a.remove(a[0])
    a.append(t)
b = tuple(a)
print(b)
#w6a4
Pythons = input().split()
result = {}
for pair in s:
    key, value = pair.split(":")
    if key not in result:
        result[key] = []
    result[key].append(value)
print(result)
#w6a5
Pythona = list(map(int, input().split()))
count = {'positives': 0, 'negatives': 0, 'zeroes': 0}
for i in a:
    if i == 0:
        count['zeroes'] += 1
    elif i < 0:
        count['negatives'] += 1
    else:
        count['positives'] += 1
print(count)
#w6a6
Pythona = list(map(int, input().split()))
sum = 0
for x in a:
    sum += x
print(sum)
#w6a7
Pythondata = tuple(input().split())
print(data[0], data[-1], data[::-1])
#w6a8
Pythontext_list = input().split()
word_counts = {}
for word in text_list:
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)
#w6a9
Pythonimport ast
text1 = ast.literal_eval(input())
text2 = ast.literal_eval(input())
result = text1.copy()
for key, value in text2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value
sorted_result = dict(sorted(result.items()))
print(sorted_result)
#w6a10
Pythona = list(map(int, input().split()))
k = int(input())
b = []
for i in range(len(a)):
    if (k - a[i] in a):
        if ((a[i], k - a[i]) in b or (k - a[i], a[i]) in b or (k - a[i] == a[i] and a.index(k - a[i]) == i)):
            continue
        else:
            b.append((a[i], k - a[i]))
result = sorted(b)
print(result)
#w6a11
Pythona = list(map(int, input().split()))
odd = ()
even = ()
for x in a:
    if x % 2 == 0:
        even += (x,)
    else:
        odd += (x,)
print(even)
print(odd)
#w6a12
Pythonnumber = list(map(int, input().split()))
counts = {}
for num in number:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
result_num = number[0]
max_freq = counts[number[0]]
for key, value in counts.items():
    if value > max_freq:
        result_num = key
        max_freq = value
    elif value == max_freq and key < result_num:
        result_num = key
print(result_num)
#w6a13
Pythonraw_input = input().split()
old_dict = {raw_input[i]: raw_input[i+1] for i in range(0, len(raw_input), 2)}
new_dict = {v: k for k, v in old_dict.items()}
print(new_dict)
#w6a14
Pythona = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for x in a:
    if x in b and x not in c:
        c.append(x)
print(c)
#w6a15
Pythonraw_data = input().split()
k = int(input())
scores = {raw_data[i]: int(raw_data[i+1]) for i in range(0, len(raw_data), 2)}
result = {key: val for key, val in scores.items() if val > k}
print(result)
#w6a19
Pythona = list(map(int, input().split()))
print(max(a))
#w6a20
Pythona = list(map(int, input().split()))
k = int(input())
if k in a:
    print(a.index(k) + 1)
else:
    print(-1)
#w6a21
Pythona = input().split()
result = {}
for i in range(len(a)):
    result[a[i]] = result.get(a[i], ()) + (i,)
print(result)
#w6a22
Pythona = list(map(int, input().split()))
print(a.index(max(a)) + 1)