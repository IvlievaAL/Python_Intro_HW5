# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum_of_two_numbers_recursia(first_n, second_n):
    if first_n == 0:
        return second_n
    elif second_n == 0:
        return first_n
    else:
        if second_n == 0:
            return first_n
        first_n += 1
        second_n -= 1
        return sum_of_two_numbers_recursia(first_n, second_n)


first_n = input("Введите первое число: ")
second_n = input("Введите второе число: ")
if first_n.isdigit() == False or second_n.isdigit() == False:
    raise TypeError ("Вводите только неотрицательные числа!")
else:
    first_n = int(first_n)
    second_n = int(second_n)
    our_sum = sum_of_two_numbers_recursia(first_n, second_n)
    print(our_sum)