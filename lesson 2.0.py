new_list = [1,2,3,4]
mix_list = [12, 3.14, 'text']
print(len(new_list))
print(new_list[0])
print(new_list[-1])
print(new_list[2:])

list_1 = ['anna', 'alex', 'max']
list_2 = ['john', 'nicolas', 'vlad']
print(list_1 + list_2)
list_1[0] = 'artur'
print(list_1)
list_1.append('anna')
print(list_1)
list_1.insert(1, 'john')
print(list_1)
print(list_1.index('max'))
list_1.index('max', 0, 10)
pop_del = list_1.pop()
print(pop_del)
print(list_1)
list_1.pop(0)
print(list_1)
list_1.clear()
print(list_1)

list_3 = ['33', '22', '11', '44']
print(list_3)
list_3.sort()
print(list_3)
list_3.sort(reverse=True)
print(list_3)

list_4 = ['abcde', 'bcb', 'da', 'cde',  'ser', 'q']
print(list_4)
list_4.sort()
print(list_4)
list_4.sort(key=len)
print(list_4)
list_4.reverse()
print(list_4)

students = {
    'alex' : 258,
    'max' : 227,
    'anna' : 278
}
print(students)
print(students['anna'])
print(students.get('alex'))
students['andrey'] = 268
print(students)
students['andrey'] = 177
print(students)
students.setdefault('oleg')
print(students)
students.pop('oleg')
print(students)
print(students.keys())
print(type(students.keys()))
key_list = list(students.keys())
print(key_list)
print(type(key_list))
print(students.values())
print(type(students.values()))
print('anna' in students)
print('peter' not in students)

a = ('alex', 22, True)
print(a)
print(type(a))
print(a[0])
print(a[0:2])
b = list(a)
print(b)
print(type(b))
c = tuple(b)
print(c)
print(type(c))

first_set = {'Alex', 'John', 'Georg', 'Alex'}
print(type(first_set))
print(first_set)
print(len(first_set))
first_set.add('Maxim')
print(first_set)
print('Maxim' in first_set)
first_set.remove('Alex')
print(first_set)
first_set.clear()
print(first_set)

first_set = {'Alex', 'John', 'Georg', 'Alex'}
second_set = {'Anton', 'Tom', 'Anna', 'Alex'}
third_set = first_set.union(second_set)
print(third_set)
fourth_set = first_set.intersection(second_set)
print(fourth_set)
fifth_set = first_set.difference(second_set)
print(fifth_set)
print(fifth_set - second_set)

set1 = {1,2,3}
set2 = {1,2,3,4,5}
print(set1.issubset(set2))
print(set2.issuperset(set1))
#print(set1[0])

if True:
	print('true')
elif True:
	print('true')
else:
	print('else')

print('Введите число от 1 до 10')
x = int(input())

if x < 4:
    print('число меньше четырех')
elif x == 5:
    print('число равно 5')
elif 10 > x > 6:
    if 8 > x > 6:
        print('число равно 7')
    elif 9 > x > 7:
        print('число равно 8')
    else:
        print('число равно 9')

else:
    print('??? введите корректное число')

