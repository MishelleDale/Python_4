# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
lst_new = []
[lst_new.append(i) for i in lst if i not in lst_new]
print(f"Список неповторяющихся элементов: {lst_new}")