numbers = [1,2,3,4,5]
print(numbers)

for i in numbers:
	print(i)
for i in numbers:
	print(i*i)

numbers = range(1,6)
for i in numbers:
	print(i)

numbers = range(1,16)
print(numbers)

new_list = []

for i in numbers:
	new_list.append(i)

print(new_list)

for i in range(1,16):
	if i % 2 == 0:
		print(f'{i} четное число')
	else:
		print(f'{i} нечетное число')

numbers = [1,2,3,4,5]

for x, item in enumerate(numbers):
	numbers[x] += 10
print(numbers)

name = 'Alex Jhonson'
for x in name:
	print(x)

for _ in range(15):
	print('Ошибка!')

some_tuple = (11, 'Alex', 3.14)
for x in some_tuple:
	print(x)

some_list = [('John', 22), ('Alex', 33), ('Artem', 44)]

for (name, age) in some_list:
	print(f'{name} is {age} years old')

some_dict = {
	'Alex': 111,
	'Maxim': 222,
	'Anna': 333
}
for x in some_dict:
	print(x)
for x in some_dict.items():
	print(x)
print(type(x))

for x, y in some_dict.items():
	print(f'Ключ {x} Значение {y}')\

for value in some_dict.values():
	print(value)


import time
'''

x = 1
while True:
    x = x+x
    print(x)
    time.sleep(1)
'''

x = 0
while x < 6:
	print(f'x равно {x}')
	x+=1
	time.sleep(0.5)
else:
	print('Завершено')

vals = [1,2,3,4,5,6,7,8,9]

summa = 0
for x in vals:
	if x % 2 == 0:
		continue
	else:
		summa += x
	if summa > 10:
		break
print(summa)

while True:
    pass