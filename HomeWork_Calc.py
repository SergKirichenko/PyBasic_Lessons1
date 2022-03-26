print(" Hello!\nЗадание калкулятор")
#############################################################################################
half_res = None
loop_op = True
##############################################################################################
while loop_op:

    first_num = input(" Input First number: ")
    operator = input("Сhoose the operation:\n 1: +\n 2: -\n 3: *\n 4: /\n 5: ^\n  Operation: ")
    second_num = input(" Input Second number: ")
    operator_f = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^"}       # вне классная работа для красоты
###############################################################################################
    try:
        operator_a = int(operator)
    except(TypeError, KeyError, NameError, ValueError):
        print("!!!Error!!! - Choose Correct Operator")

    try:
        first_in = float(first_num)
        second_in = float(second_num)

    except(TypeError, KeyError, NameError, ValueError):
        print("!!!Error!!! - Input Correct Number")
    try:
        half_res = f"{first_in} {operator_f[operator]} {second_in} = "  #
    except (TypeError, KeyError, NameError, ValueError):
        print("!!!Error!!! -   Не правилный ввод ")
##############################################################################################
    try:
        if operator == "1":                               # операция слложения
            result = first_in + second_in
            print(f"Result :\n  {half_res} {result}")
        elif operator == "2":                              # операция вычетания
            result = first_in - second_in
            print(f"Result :\n  {half_res} {result}")
        elif operator == "3":                              # операция умножения
            result = first_in * second_in
            print(f"Result :\n  {half_res} {result}")
        elif operator == "4":                              # операция деления
            result = first_in / second_in
            print(f"Result :\n  {half_res} {result}")
        elif operator == "5":                              # операция возведения в степень
            result = first_in ** second_in
            print(f"Result :\n  {half_res} {result}")
        else:
            print("!!!Error!!! - Choose 1-5 Operator")
    except (NameError, ZeroDivisionError, TypeError, OverflowError):
        print("!!!Error!!! - раскладка клавиатуры | Не правельный ввод данный | Деление на 0 | Очень болшое число")
###################################################################################
    loop = input("  Press Any Key to try again. Press 'n' to quit: ")
    loop_op = True if loop != "n" else False
print(" The End ")
