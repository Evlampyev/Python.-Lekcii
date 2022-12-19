def Even(n):
    if n % 2 == 0:
        s = "Чётное"
    else:
        s = "Нечётное"
    return print(s)


def MyPower(number, level):
    return number ** level


def NewString(symbol, count=3):  # 3 - значение по умолчанию, то есть если не указано
    return symbol * count


def Concatenatio(*param):
    res: str = ""  # переменная res - тип строка
    for item in param:
        res += item
    return res


def Fibonachi(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonachi(n - 1) + Fibonachi(n - 2)
