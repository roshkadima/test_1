x = input('ticket')

y = x
a = len(x)

if (a % 2 == 0):
     t = y[:len(x) // 2]
     g = y[len(x) // 2:]

     b = sum(map(int,t ))
     c = sum(map(int,g ))

     if b == c:
         print('lucky ticket ')
     else:
         print('not a lucky ticket')
else:
    print('error')

print('exercise 2')

x = input('palindrome ')

y = x
a = len(x)

if (a % 2 == 0):
    t = y[:len(x) // 2]
    g = y[len(x) // 2:]

    h = list(t)
    c = (list(reversed(g)))

    if c == h:
        print('palindrome')
    else:
        print('not palindrome')
else:
    print('error')