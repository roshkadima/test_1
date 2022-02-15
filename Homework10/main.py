def max_number(x):
    max_ = x[0]
    for ele in x:
        if ele > max_:
           max_ = ele
    return max_


list1 = [1,6,3,2,8,]
result = max_number(list1)
print(result)

#exercise 2

def summa(a, b):
    c = a + b
    return c

print(summa(100,2))

#exercise 3

def cube(x,y):
    res = '*' * x + '\n' +('*' + ' ' * (y - 2) + '*' + '\n') * (x - 2) + '*' * y
    return res
print(cube(5,5))

#exercise 4

def LinearSearch(x, element):
    for i in range (len(x)):
        if x[i] == element:
            return i
    return -1

print(LinearSearch([1,2,3,4,5,2,1], 7))


#exercise 5

def number_words(x):
    x = input()
    x = x.split()
    b = len(x)
    return
