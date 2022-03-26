
loop_op = True
while loop_op:
    qwest = input("Выбери номер задание на выполнение: 1 | 2 | 3 | 4 | 5 | \n  Выбраный номер: ")

# 111###########################################
    if qwest == "1":
        try:
            value = int(input("Ввкдите целое число: "))
            new_value = value / 2 if value < 100 else -value
            print(new_value)
        except (TypeError, NameError, ValueError):
            print(" Ошибка - это не целое число")

# 222#############################################
    elif qwest == "2":
        try:
            value = int(input("Ввкдите целое число: "))
            new_value = 1 if value < 100 else 0
            print(new_value)
        except (TypeError, NameError, ValueError):
            print(" Ошибка - это не целое число")

# 333################################################
    elif qwest == "3":
        try:
            value = int(input("Ввкдите целое число: "))
            new_value = True if value < 100 else False
            print(new_value)
        except (TypeError, NameError, ValueError):
            print(" Ошибка - это не целое число")

# 444#################################################
    elif qwest == "4":
        my_str = input("Введи слово:  ")
        index = 5
        if index > len(my_str):
            result = my_str + my_str
        else:
            result = my_str
        print(result)

# 555#################################################
    elif qwest == "5":
        my_str = input("Введи слово:  ")
        index = 5
        if index > len(my_str):
            result = my_str + my_str[::-1]
        else:
            result = my_str
        print(result)

#####################################################
    else:
        print(" Не правилный выбор ")
    loop = input("  Press Any Key to try again. Press 'n' to quit: ")
    loop_op = True if loop != "n" else False
print("  Конец   ")
