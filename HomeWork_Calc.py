print("Hello!!!\nЗадание калкулятор")
#############################################################################################
half_res = None
##############################################################################################
first_num = input(" Input First number: ")
try:
    first_in = float(first_num)
except (ValueError, NameError):
    print("!!!Incorrect number!!!")
###############################################################################################
operator = input("Сhoose the operation:\n 1: +\n 2: -\n 3: *\n 4: /\n 5: ^\n  Operation: ")
try:
    operator_a = int(operator)
except:
    print("!!!Error!!! - Choose Correct Operator")
###############################################################################################
second_num = input(" Input Second number: ")
try:
    second_in = float(second_num)
except (ValueError, NameError):
    print("!!!Incorrect number!!!")
##############################################################################################
operator_f = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^"}       # вне классная работа для красоты
try:
    half_res = f"{first_in} {operator_f[operator]} {second_in} = "    #
except (TypeError, KeyError,NameError):
    print("!!!Error!!! - Choose Correct Operator /  Не правилный ввод ")
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
        if first_in and second_in != 0:                   # проверка на 0 внутри блока
            result = first_in / second_in                 #
            print(f"Result :\n  {half_res} {result}")     #
        else:                                             #
            print("!!!Error!!! - Zero Divide")                  #
    elif operator == "5":                              # операция возведения в степень
        result = first_in ** second_in
        print(f"Result :\n  {half_res} {result}")
    else:
        print("!!!Error!!! - Choose Correct Operator")
except NameError:
    print("!!!Error!!! - раскладка клавиатуры | Не правельный ввод данный")
###################################################################################