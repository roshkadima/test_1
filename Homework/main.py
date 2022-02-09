x = input('x=')
x1 = input('x1=')
y = set(x)
y1 = set(x1)

print(y & y1)

print('='*10)

a = [i for i in range(3,100,3)]

x = [i for i in range(5,100,5)]

x1 = set(x)
a1 = set(a)

print(a1 & x1)