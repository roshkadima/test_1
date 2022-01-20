#exercise 2.1
x = int(input('x'))
if x < 0:
    print(x)
else:
    print('error')

#exercise 2.2
print('==========exercise 2.2==========')

x = int(input('x='))

if x < 20:
    print('less 20')
elif x == 20:
    print('exactly 20')
else:
    print('more 20')

#exercise 2.3
print('==========exercise 2.3==========')

x = int(input('x='))
if x == 0:
    print('given number is Zero')
else:
    print('given number not is Zero')

# exercise 2.4
print('==========exercise 2.4==========')

print('Even'if int(input('x=')) % 2 == 0 else'Odd')

# exercise 2.5
print('==========exercise 2.5==========')

a, b, c = int(input('a = ')), int(input('b = ')), int(input('c = '))

if b > a:
    a = b
if c > a:
    a = c
print(a)