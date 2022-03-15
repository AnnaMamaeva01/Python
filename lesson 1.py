print('Hello world')
#print('Hello world 2') коммент
'''
Коммент
print('Hello world 2')
'''
print('Hello world 2')

x = 1
print(x)
print(type(x))
x = float(x)
print(x)
print(type(x))

x = 3
print(x)
x = 5
print(x)
y = 4
print(x + y)
print(y + y)
print(x + x)
print(type(x))
z = 'text123'
print(type(z))

#print(x + z)

print(z + ' ' + z)
x = None
print(type(x))

print(x)
x = 1+1
x = 2+2
x = 3-2
x = 3-5
x = 9/3
x = 1/1
x = 7/2
x = 3.0+1
x = 3*2
x = 1.2*3
x = round(1.2*3, 2)

x = 3%2
x = 4%2==0
x = 9%2==0
x = 2*2*2*2
x = 2**4

x = 2+2*2
x = (2+2)*2
x = (2+2)*2+3*(6/2)
x = 3**36
x = 2**62
print(x)

import math
a = 15
b = 11
c = 9

p = (a+b+c)/2

s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)

import math
pi = 3.14
R = 12
S = pi*R**2
print(S)

x = int(True)
print(x)

y = int(False)
print(y)

a = []
b = [1, 2, 3]

x = bool(a)
print(x)

y = bool(b)
print(y)

a = True
print(a)
print(type(a))
#b = true

print(2>3)
print(3<2)
print(2>1)

print(2>=2)
print(3>=2)
print(2>=3)

print(1!=1)
print(2!=1)
print(1==1)
print(2==1)

print('text' == 'text') #True
print('text' == 'text 2') #false
print('text' == 'TEXT') #false

print(1<2<3<4) #True
print(1<2<3>4) #false

print(1<2 and 2<3) #True
print(1>2 and 2<3) #false
print(1>2 or 2<3) #True
print(1>2 or 2>3) #false

x = 'Alex'
print(x)
y = "Some text 123"
print(y)
#z = 'Some 'long' text'
z = "Some 'long' text"
print(z)

x = "Some 'long', and 'awesome' text"
print(x)

#x = "Some \'long\', and \'awesome\' text"
print(x)
y = 'C:\\Users\\dell\\Desktop\\Py_lesson'
print(y)
z = r'C:\Users\dell\Desktop\Py_lesson'
print(z)
x = 'some long text \nand new string \nand new string \nand new string'
print(x)

text = str('hello world')
print(text)
print(text[0])
print(text[0]+text[1])
print(text[-1]+text[1])
print(text[6:]+text[1])
print(text[6:]+' '+text[:6])
print(text[6:8])
print(text[::1])
print(text[::2])

x = 'some long and awesome TEXT'
print(len(x))
print(x[len(x)-1])
print(x[len(x)-4:len(x)])
print(x.count('o'))
print(x.find('a'))
print(x.find('o'))
print(x.find('o'))
print(x.find('o', 3, 7))
print(x.find('o', 7))
print(x.find('and'))
print(x.find('TEXT'))
print(x.find('abc'))

x = 'some long and awesome TEXT'
print(len(x))
print(x[len(x)-1])
print(x[len(x)-4:len(x)])
print(x.count('o'))
print(x.find('a'))
print(x.find('o'))
print(x.find('o'))
print(x.find('o', 3, 7))
print(x.find('o', 7))
print(x.find('and'))
print(x.find('TEXT'))
print(x.find('abc'))
print(x.capitalize())
print(x.upper())
print(x.lower())
print('Old text: '+x)
upper_cased = x.upper()
lower_cased = x.lower()
print(upper_cased.isupper())
print(lower_cased.islower())
print(x.isupper())
print(x.islower())

print('xxx777'.isalnum())
print('xxx777!'.isalnum())
print('xxx777'.isalpha())
print('xxx'.isalpha())

x = str('hello')
print(x.startswith('he'))
print(x.endswith('lo'))
split = x.split('l')
print(type(split))
print(split)
split = x.split('e')
print(split)

some_data = '4;8;15;16;23;42'
separated_data = some_data.split(';')
print(separated_data)
print(separated_data[3])

x = '10'
y = 'cold'
print('Weather: temperature +{} and it\'s {}'.format(x, y))
print('Weather: temperature +{1} and it\'s {0}'.format(x, y))
print(f'Weather: temperature +{x} and it\'s {y}')