import task1
import task2
import task3

def main_menu():
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
