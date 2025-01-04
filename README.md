# 9-11laba
import task1
import task2
import task3

def main_menu():
    """
    Основное меню программы, которое позволяет пользователю выбрать задание.
    """
    while True:
        print("\nГлавное меню:")
        print("1. Задание 1: Сумма чисел из двух массивов")
        print("2. Задание 2: Проверка суммы чисел из трех массивов")
        print("3. Задание 3: Поворот матрицы на 90 градусов")
        print("4. Завершение работы программы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            task1.main()
        elif choice == '2':
            task2.main()
        elif choice == '3':
            task3.main()
        elif choice == '4':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")

if __name__ == "__main__":
    main_menu()
import numpy as np
import random

def generate_random_array(size):
    """
    Генерирует массив случайных чисел заданного размера.

    :param size: Размер массива
    :return: Массив случайных чисел
    """
    return np.random.randint(0, 10, size)

def input_array(size):
    """
    Ввод массива от пользователя.

    :param size: Размер массива
    :return: Массив, введенный пользователем
    """
    array = list(map(int, input(f"Введите {size} элементов массива через пробел: ").split()))
    if len(array) != size:
        print(f"Ошибка: введите ровно {size} элементов.")
        return None
    return np.array(array)

def sum_arrays(array1, array2):
    """
    Суммирует элементы двух массивов. Если элементы совпадают, их сумма равна нулю.

    :param array1: Первый массив
    :param array2: Второй массив
    :return: Результирующий массив
    """
    return np.array([a + b if a != b else 0 for a, b in zip(array1, array2)])

def main():
    """
    Основная функция для задания 1.
    """
    array1 = None
    array2 = None
    result = None

    while True:
        print("\nМеню задания 1:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Вернуться в главное меню")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            size = int(input("Введите размер массивов: "))
            print("Выберите способ ввода данных:")
            print("1. Вручную")
            print("2. Сгенерировать случайным образом")
            input_method = input("Выберите способ ввода: ")

            if input_method == '1':
                array1 = input_array(size)
                array2 = input_array(size)
            elif input_method == '2':
                array1 = generate_random_array(size)
                array2 = generate_random_array(size)
            else:
                print("Неверный выбор.")
                continue

            if array1 is not None and array2 is not None:
                print("Массив 1:", array1)
                print("Массив 2:", array2)
                result = None  # Сброс результата

        elif choice == '2':
            if array1 is not None and array2 is not None:
                array1_sorted = np.sort(array1)[::-1]
                array2_sorted = np.sort(array2)
                result = sum_arrays(array1_sorted, array2_sorted)
                result = np.sort(result)
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите исходные данные.")

        elif choice == '3':
            if result is not None:
                print("Результат:", result)
            else:
                print("Сначала выполните алгоритм.")

        elif choice == '4':
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")
import numpy as np
import random

def generate_random_array(size):
    """
    Генерирует массив случайных чисел заданного размера.

    :param size: Размер массива
    :return: Массив случайных чисел
    """
    return np.random.randint(0, 10, size)

def input_array(size):
    """
    Ввод массива от пользователя.

    :param size: Размер массива
    :return: Массив, введенный пользователем
    """
    array = list(map(int, input(f"Введите {size} элементов массива через пробел: ").split()))
    if len(array) != size:
        print(f"Ошибка: введите ровно {size} элементов.")
        return None
    return np.array(array)

def check_sums(array1, array2, array3):
    """
    Проверяет, могут ли два числа под одним и тем же номером в сумме давать третье число.
    Если могут, то сумма трех чисел возводится в степень наименьшего числа.

    :param array1: Первый массив
    :param array2: Второй массив
    :param array3: Третий массив
    :return: Результирующий массив
    """
    result = []
    for a, b, c in zip(array1, array2, array3):
        if a + b == c:
            result.append((a + b + c) ** min(a, b, c))
    return result

def main():
    """
    Основная функция для задания 2.
    """
    array1 = None
    array2 = None
    array3 = None
    result = None

    while True:
        print("\nМеню задания 2:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Вернуться в главное меню")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            size = int(input("Введите размер массивов: "))
            print("Выберите способ ввода данных:")
            print("1. Вручную")
            print("2. Сгенерировать случайным образом")
            input_method = input("Выберите способ ввода: ")

            if input_method == '1':
                array1 = input_array(size)
                array2 = input_array(size)
                array3 = input_array(size)
            elif input_method == '2':
                array1 = generate_random_array(size)
                array2 = generate_random_array(size)
                array3 = generate_random_array(size)
            else:
                print("Неверный выбор.")
                continue

            if array1 is not None and array2 is not None and array3 is not None:
                print("Массив 1:", array1)
                print("Массив 2:", array2)
                print("Массив 3:", array3)
                result = None  # Сброс результата

        elif choice == '2':
            if array1 is not None and array2 is not None and array3 is not None:
                result = check_sums(array1, array2, array3)
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите исходные данные.")

        elif choice == '3':
            if result is not None:
                print("Результат:", result)
            else:
                print("Сначала выполните алгоритм.")

        elif choice == '4':
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")
import numpy as np
import random

def generate_random_matrix(n, m):
    """
    Генерирует матрицу случайных чисел заданного размера.

    :param n: Количество строк
    :param m: Количество столбцов
    :return: Матрица случайных чисел
    """
    return np.random.randint(0, 10, size=(n, m))

def input_matrix(n, m):
    """
    Ввод матрицы от пользователя.

    :param n: Количество строк
    :param m: Количество столбцов
    :return: Матрица, введенная пользователем
    """
    matrix = []
    print(f"Введите элементы матрицы {n}x{m} через пробел:")
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            print(f"Ошибка: введите ровно {m} элементов.")
            return None
        matrix.append(row)
    return np.array(matrix)

def rotate_matrix(matrix, direction):
    """
    Поворачивает матрицу на 90 градусов в заданном направлении.

    :param matrix: Исходная матрица
    :param direction: Направление поворота (clockwise/counterclockwise)
    :return: Повернутая матрица
    """
    if direction == 'clockwise':
        return np.rot90(matrix, -1)
    elif direction == 'counterclockwise':
        return np.rot90(matrix, 1)
    else:
        return matrix

def main():
    """
    Основная функция для задания 3.
    """
    matrix = None
    result = None

    while True:
        print("\nМеню задания 3:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Вернуться в главное меню")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            n = int(input("Введите количество строк матрицы: "))
            m = int(input("Введите количество столбцов матрицы: "))
            print("Выберите способ ввода данных:")
            print("1. Вручную")
            print("2. Сгенерировать случайным образом")
            input_method = input("Выберите способ ввода: ")

            if input_method == '1':
                matrix = input_matrix(n, m)
            elif input_method == '2':
                matrix = generate_random_matrix(n, m)
            else:
                print("Неверный выбор.")
                continue

            if matrix is not None:
                print("Матрица:")
                print(matrix)
                result = None  # Сброс результата

        elif choice == '2':
            if matrix is not None:
                direction = input("Выберите направление поворота (clockwise/counterclockwise): ")
                result = rotate_matrix(matrix, direction)
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите исходные данные.")

        elif choice == '3':
            if result is not None:
                print("Результат:")
                print(result)
            else:
                print("Сначала выполните алгоритм.")

        elif choice == '4':
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")
