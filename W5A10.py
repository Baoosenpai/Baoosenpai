def check(a,b):
    a_to_b = {}
    b_mapped_to = set()
    for char_a,char_b in zip(a,b):
        if char_a in a_to_b:
            if a_to_b[char_a] != char_b:
                return False
        elif char_b in b_mapped_to:
            return False
        a_to_b[char_a] = char_b
        b_mapped_to.add(char_b)
    return True
x,y = input().split()
if check(x,y):
    print('true')
else:
    print('false')
