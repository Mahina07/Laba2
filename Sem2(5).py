def func():
    n = int(input('Введите число от 0 до 100000: '))
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True
print(func())