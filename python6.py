from math import *
from fractions import *
print('hieu','vnpay',sep='-')
t="""hieu
2001"""
print(type(t))
a  = 1.289436
print('%.2f'%a)
c=5
b=2
print(gcd(c,b))
strA = 'Trần Trung \n Hiếu'
strB = 'Hiếu'
strC = strB in strA
print(strA[-2])
print(len(strA))
print(factorial(c))
print(f'giá trị a + b: {a} + {b} = {a+b}')
print(strA[5:10])
print(c//b)
print(c%b)

list_a = [1, 3, 4, 2, 4] 
list_a.sort(reverse=True)
print(list_a)
print(sum(list_a) / len(list_a))
print(set(list_a))
list_b = list_a + list_a
print(list_b)
del(list_a[3])
list_a.append(9)
list_a.insert(3,15)
print(list_a)

tuple_a = (1,2,3)

set_a = set(list_b)
print(set_a)
set_b = {3,4,5,6}
set_a.add(80)
set_a.remove(80)
print(set_a | set_b)
print(set_a & set_b)

dictionary_a = {'name': 'Hiếu','age':25}
dictionary_a['company'] = 'NGV'
dictionary_a['age'] = 24
print(dictionary_a.values())

if 8 in set_a:
    print(set_a)
elif 7 in set_b:
    print(set_b)
else:
    print('NO')

for i in range(1,c,2): # range(5): mặc định từ 0 --> 5, khoảng cách là 1
    if i == 3: 
        break
    print(i)

while True:
    try:
        gtri1 = int(input('Nhập giá trị đầu vào'))
        print(5/gtri1)
    except ZeroDivisionError as e:
        print(f'Lỗi: {e}')
    else: 
        print('ok')
        break


class Chia_chinh_minh(Exception):
    pass

while True:
    try:
        gtri1 = int(input('Nhập giá trị đầu vào: '))
        if gtri1 == 5:
            raise Chia_chinh_minh("Không được chia cho chính mình") #raise Chia_chinh_minh() cũng được nhưng sẽ ko có thông báo gì
        print(5 / gtri1)
    except ZeroDivisionError as e1:
        print(f'Lỗi: {e1}')
    except Chia_chinh_minh as e2:
        print(f'Lỗi: {e2}')
    else:
        break
    finally:
        print('đã xong')
        