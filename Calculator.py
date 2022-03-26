print(" Задание калкулятор")
#############################################################################################
result = ()
operator_r = None
first_in = None
second_in = None
half_res = None
calc_loop = True
##############################################################################################
while calc_loop:
    first_val = input(" Input First number: ")
    second_val = input(" Input Second number: ")
    operator = input("Сhoose the operation:  1: + || 2: - || 3: * || 4: / || 5: ^ |\n  Operation: ")
    operator_f = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^"}                         # библиотека
##############################################################################################
    if operator in ("1", "2", "3", "4", "5"):
        try:
            first_in = float(first_val)
            second_in = float(second_val)
        except (NameError, ValueError):
            print(" !! Error !! - Wrong Input numbers ")

        try:
            half_res = f"{first_in} {operator_f[operator]} {second_in} = "  # для красоты
            operator_r = int(operator)
        except (NameError, ValueError, TypeError, KeyError):
            print("!! Error !! - Choose Correct Operator from 1-5 ")
        try:
            result_1 = first_in + second_in
            result_2 = first_in - second_in
            result_3 = first_in * second_in
            result_4 = first_in / second_in
            result_5 = first_in ** second_in
            result = (result_1, result_2, result_3, result_4, result_5)  # список

            print("  Result: ", half_res, result[operator_r - 1])  # срез списка
        except (TypeError, ZeroDivisionError, IndexError, OverflowError):
            print("!!!Error!!! - Input Correct Value /  Очень болшое число  / Деление на 0")

    else:
        print("  Choose Operator from 1 - 5 ")
    loop = input("  Press Any Key to try again. Press 'n' to quit: ")
    calc_loop = True if loop != "n" else False
################################################################################################
print("\n  End Calculator ")
