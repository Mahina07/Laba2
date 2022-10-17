def Func():
    x = int(input('Введите число: '))
    n = int(input('Введите степень квадратного корня: '))
    x_k = 1
    x_k1 = (1 / n) * ((n - 1) * x_k + x / x_k ** (n - 1))
    while abs(x_k1 - x_k) > 0.00001:
        x_k = x_k1
        x_k1 = (1 / n) * ((n - 1) * x_k + x / x_k ** (n - 1))
    return x_k1
print(Func())