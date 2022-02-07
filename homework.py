res = {1:'Mondey',2:'Tuesday', 3:'Wednesday',4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}

x = res.get(1)

print(x)

print('=' * 10)
#exercise 2

x = {
    'name': 'Cat',
    'age': 3,
    'color': 'black',
    'species': 'British shorthair cat '
}

print(x['age'])

print('=' * 10)

#exercise 3
x = input('word:')

res = {}

for item in x:
    if res.get(item):
        res[item] += 1
    else:
        res[item] = 1

print(res)

print('=' * 10)

