# в файле 1.txt набор чисел. Необходимо выбрать из них четные и составить пары: число и его квадрат.
import random

data = open('1.txt', 'w')
s = ''
for i in range(10):
    s += str(random.randint(1, 20)) + ' '
print(s)
data.writelines(s)
data.close()

data = open('1.txt', 'r')
s = data.read() + ' '
data.close()
res = list(map(int,
               s.split()))  # map - применяет функцию к каждому элементу следующего аргумента, результат лучше в список положить
res = list(filter(lambda x: not x % 2, res))  # filter - фильтрует элементы по функции, результат лучше в список
res = list(map(lambda x: (x, x ** 2), res))  # lambda - анонимная фунция, для упрощения, если ипользуется однажды,
                                            # до : - входные параметры,
                                            # после - что после return
print(res)
