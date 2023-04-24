# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def a_in_degree_b(a, b, nashe_a):
    if b == 1:
        return a
    a = a*nashe_a
    b -= 1
    return a_in_degree_b(a, b, nashe_a)

a = int(input("Введите число a: "))
nashe_a = a
b = int(input("Введите число b: "))
print(a_in_degree_b(a, b, nashe_a))