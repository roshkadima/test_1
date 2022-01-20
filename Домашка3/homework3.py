# exercise 3
print('side: ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('Triangle exists ')
else:
    print('triangle does not exist')