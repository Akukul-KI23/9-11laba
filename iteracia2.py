import numpy as np
import random

def generate_random_array(size):
    return np.random.randint(0, 10, size)

def input_array(size):
    array = list(map(int, input(f"Введите {size} элементов массива через пробел: ").split()))
    if len(array) != size:
        print(f"Ошибка: введите ровно {size} элементов.")
        return None
    return np.array(array)

def check_sums(array1, array2, array3):
    result = []
    for a, b, c in zip(array1, array2, array3):
        if a + b == c:
            result.append((a + b + c) ** min(a, b, c))
    return result

def main():
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
