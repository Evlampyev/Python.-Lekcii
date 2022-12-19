colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)  # разделителей не будет, все слова подряд
data.write('\n line 1 \n')
data.write('Line next |\n')
data.writelines(colors)
data.close()  # закрытие подключения к файлу

newData = open('file.txt', 'r')
for line in newData:
    print(line, end="")
newData.close()
