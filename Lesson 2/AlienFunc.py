import functions

N = int(input())
functions.Even(N)
a = int(input())
print(f'{N}^{a} = {functions.MyPower(N, a)}')

print(functions.NewString('!', 5))
print(functions.NewString('!'))
print(functions.NewString(4))

print(functions.Concatenatio('a', 's', 'd'))  # asd
print(functions.Concatenatio('a', '3'))  # a3

list = []
for i in range(1, 10):
    list.append(functions.Fibonachi(i))
print(list)

dictionary = {}  # словарь
newDictionary = \
    {
        'up': '↑',
        'down': '↓'
    }

for i in newDictionary.keys(): #распечатка ключей
    print(i)
for i in newDictionary.values(): #распечатка значений
    print(i)


