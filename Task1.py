# Вычислить число π c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d =  int(input("Введите число для заданной точности числа Пи (сколько знаком после запятой показать):\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
