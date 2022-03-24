print(" Задание калкулятор")
#############################################################################################
result = ()
operator_r = None
first_in = None
second_in = None
half_res = None
##############################################################################################
first_val = input(" Input First number: ")
second_val = input(" Input Second number: ")
operator = input("Сhoose the operation:\n 1: +\n 2: -\n 3: *\n 4: /\n 5: ^\n  Operation: ")
operator_f = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^"}
##############################################################################################
try:
    first_in = float(first_val)
    second_in = float(second_val)
    half_res = f"{first_in}{operator_f[operator]}{second_in} = "
except (NameError, KeyError, ValueError, TypeError):
    print("!!!Error!!! - Input Correct Value /  Не правилный ввод данных")
try:
    result_1 = first_in + second_in
    result_2 = first_in - second_in
    result_3 = first_in * second_in
    result_4 = first_in / second_in
    result_5 = first_in ** second_in
    result = (result_1, result_2, result_3, result_4, result_5)
    operator_r = int(operator)
    print("Result: ", half_res, result[operator_r - 1])
except (NameError, KeyError, ValueError, TypeError, ZeroDivisionError, IndexError):
    print("!!!Error!!! - Input Correct Value /  Не правилный ввод / Деление на 0")
################################################################################################
print("\n  End Calculator ")