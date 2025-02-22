"""Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно (значение, время). Определить (смоделировать) границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
24. F(0) = F(1) = 11, F(n) = (-1)n*(3*F(n–1) /(2n)!- F(n-2)!), при n > 1"""

import timeit
import matplotlib.pyplot as plt

# Функция для вычисления факториала числа
last_factorial = 1
def dynamic_factorial(n):
    global last_factorial
    last_factorial = n * last_factorial
    return last_factorial

# Рекурсивная функция для вычисления факториала
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 11
    else:
        return n * recursive_factorial(n-1)

# Итеративная функция для вычисления факториала
def iterative_factorial(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i
    return answer


F_value = 1

# Функция для вычисления значения F
sign = 1
def dynamic_F(n):
    global F_value
    if n == 0 or n == 1:
        return 11
    else:
        global sign
        sign *= -1
        F_value = sign * (3 * dynamic_F(n - 1) / dynamic_factorial(2 * n) - dynamic_factorial(dynamic_F(n - 2)))
        return F_value

# Функция для обработки времени
def score_time(func, n):
    return timeit.timeit(lambda: func(n), number=1000)

values_n = range(2, 11)
# Список значений n для которых необходимо измерить время выполнения
recursive_times = []
iterative_times = []


# Для каждого значения n измеряем время выполнения
for n in values_n:
    recursive_times.append(score_time(recursive_factorial, n))
    iterative_times.append(score_time(iterative_factorial, n))


# Вывод результатов в табличной форме
print(f"{'n':<10}{'Рекурсивное время (мс)':<25}{'Итерационное время (мс)':<25}")
for i, n in enumerate(values_n):
    print(f"{n:<10}{recursive_times[i]:<25}{iterative_times[i]:<25}")

# Построение и вывод графика результатов
plt.plot(values_n, recursive_times, label='Рекурсивно')
plt.plot(values_n, iterative_times, label='Итерационно')
plt.xlabel('n')
plt.ylabel('Время (в миллисекундах)')
plt.legend()
plt.title('Сравнение времени вычисления функции F(n)')
plt.show()