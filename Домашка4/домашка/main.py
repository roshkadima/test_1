#exercise 1
for i in range(0, 100):
    if i % 7 == 0:
        print(i)

#exercise 2
print('=========================')
n = int(input('factorial'))

f = 1
while n > 1:
    f *= n
    n -= 1

print(f)

