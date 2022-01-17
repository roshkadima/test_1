# exercise 4
print('==============================================================')
print('Plese, enter the card')
x = int(input('x='))

print('last four number', x % 10000)

# exercise 5
print('==============================================================')
print('Plese, enter three-digit number')

x = int(input('x='))

y = x // 100
c = x // 10 % 10
d = x % 10
K = y + c + d
print(K)

# exercise 6
print('==============================================================')
print('enter side "a" and height "h" , to find the area')

a = int(input('a='))
h = int(input('h='))

S = ((0.5 * a) * h)

print(S)

# exercise 7
print('==============================================================')
x = int(input("enter number: "))
y = 0
while (x != 0):
    y = y + x % 10
    x = x // 10
print("The sum of the digits of the number is : ", y)


# exercise 8
print('==============================================================')
x = input('Enter an integer:')
y = len(str(x))
print('the number of numbers in a number: ', y)

# exercise 9
print('==============================================================')
x = input("Enter an integer : ")
y = x[::-1]
print('reverse number:', y)
