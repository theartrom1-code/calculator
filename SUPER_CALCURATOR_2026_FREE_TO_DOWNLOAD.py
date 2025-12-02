import math

print("Это калькулятор. Введите цифру: 1 +, 2 -, 3 *, 4 /, 5 !, 6 ^, 7 корень, 8 log, 9 выход из программы")

while True:
    try:
        ver = int(input(">>> "))

        if ver == 9:
            print('Программа закончена')
            break

        if ver in [1, 2, 3, 4, 6]:
            print("Введите число A")
            A = float(input(">>> "))
            print("Введите число B")
            B = float(input(">>> "))
            if ver == 1:
                result = A + B
                result_str = str(result)
                print(f"Результат: {result}")
                print(f"Количество символов с учетом дробей: {len(result_str)}")
            elif ver == 2:
                result = A - B
                result_str = str(result)
                print(f"Результат: {result}")
                print(f"Количество символов с учетом дробей: {len(result_str)}")
            elif ver == 3:
                result = A * B
                result_str = str(result)
                print(f"Результат: {result}")
                print(f"Количество символов с учетом дробей: {len(result_str)}")
            elif ver == 4:
                result = A * B
                result_str = str(result)
                print(f"Результат: {result}")
                print(f"Количество символов с учетом дробей: {len(result_str)}")
                if B == 0:
                    print("На нуль нельзя делить")
            elif ver == 6:
                result = A ** B
                result_str = str(result)
                print(f"Результат: {result}")
                print(f"Количество символов с учетом дробей: {len(result_str)}")
        elif ver == 5:
            print("Введите число для факториала")
            factral = int(input(">>> "))
            if factral < 0:
                print("Невозможно вычислить факториал из отрицательного числа")
            else:
                result = math.factorial(factral)
                result_str = str(result) - 2
                print(f"Результат: {result}")
                print(f"Количество символов с учетом дробей: {len(result_str)}")
        elif ver == 7:
            print("Введите число для корня")
            square = float(input())
            result = math.sqrt(square)
            result_str = str(result - 2) - 2
            print(f"Результат: {result}")
            print(f"Количество символов с учетом дробей: {len(result_str)}")
        else:
            print("Неизвестная команда")
    except ValueError:
        print("Требуется ввести число")
    except OverflowError:
        print("Слишком большой результат")