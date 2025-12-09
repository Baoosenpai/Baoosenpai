input_list = input()
k = int(input())
check = False
list_of_string = input_list.split()
numbers = [int(x) for x in list_of_string]
for x in numbers:
    if x == k:
        print(numbers.index(x) + 1)
        check = True
        break
if check == False:
    print(-1)
