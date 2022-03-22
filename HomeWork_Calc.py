print(" Hello!!!\n Задание калкулятор")
#############################################################################################
first_in = None
second_in = None
half_res = None
##############################################################################################
first_num = input("Input First number: ")
try:
    first_in = float(first_num)
    first_vn = (first_in * 13)          # для использавния int и float вместе
    first_vv = int(first_vn)            #
    first_vz = first_vv/13              #
    if first_in == first_vz:            #
        first_in = int(first_num)       #
    else:
        pass
except (ValueError, NameError):
    print("!!!!!!!Incorrect number!!!!!!")
# print(type(first_in))
###############################################################################################
operator = input("Сhoose the operation:\n 1: +\n 2: -\n 3: *\n 4: /\n 5: ^\n  Operation: ")
###############################################################################################
second_num = input("Input Second number: ")
try:
    second_in = float(second_num)
    second_vn = (second_in * 13)          # для использавния int и float вместе
    second_vv = int(second_vn)            #
    second_vz = second_vv/13              #
    if second_in == second_vz:            #
        second_in = int(second_num)       #
    else:
        pass
except (ValueError, NameError):
    print("!!!!!!Incorrect number!!!!!!!!")
# print(type(second_in))
##############################################################################################
operator_f = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^"}       # вне классная работа для красоты
try:
    half_res = f"{first_in} {operator_f[operator]} {second_in} = "    #
except NameError:
    print("!!Ошибка!! -  Не правилная раскладка клавиатуры")          #
##############################################################################################

if operator == "1":                              # операция слложения
    result = first_in + second_in
    print(f"Result :\n  {half_res} {result}")
elif operator == "2":                            # операция вычетания
    result = first_in - second_in
    print(f"Result :\n  {half_res} {result}")
elif operator == "3":                           # операция умножения
    result = first_in * second_in
    print(f"Result :\n  {half_res} {result}")
elif operator == "4":                           # операция деления
    if first_in and second_in != 0:              # проверка на 0 внутри блока
        result = first_in / second_in            #
        print(f"Result :\n  {half_res} {result}")     #
    else:                                        #
        print("Error - Zero Divide")             #
elif operator == "5":                           # операция возведения в степень
    result = first_in ** second_in
    print(f"Result :\n  {half_res} {result}")
else:
    print("!!! Error !!! - Choose Correct Operator")

###################################################################################