# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите число N: \n')) #нужен int тип

i = 2 # первое простое число
lst = [] #задаем список
start_number = N
while i <= N:
    if N % i == 0:
        lst.append(i)
        N //= i
        i = 2  #чтобы не потерять порядок 2
    else:
        i += 1
print(f"Простые множители числа {start_number}: {lst}")