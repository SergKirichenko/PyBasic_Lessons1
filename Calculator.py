print("\n Calculator ")
#############################################################################################
calc_loop = True
result = None
sign = None
##############################################################################################
while calc_loop:
    operator = input("Select the operation: | 1: + || 2: - || 3: * || 4: / || 5: ^ |\n  Operation: ")
    if operator in "12345":
        try:
            first_in = float(input(" Input First number: "))
            second_in = float(input(" Input Second number: "))
            if operator == "1":
                result = first_in + second_in
                sign = "+"
            elif operator == "2":
                result = first_in - second_in
                sign = "-"
            elif operator == "3":
                result = first_in * second_in
                sign = "*"
            elif operator == "4":
                result = first_in / second_in
                sign = "/"
            elif operator == "5":
                result = first_in ** second_in
                sign = "^"
            print(f"  Result:  {first_in} {sign} {second_in} = {result}")
        except (TypeError, NameError, ValueError):
            print(" !! Error !! - Wrong Input numbers ")
        except ZeroDivisionError:
            print("!!!Error!!! - Zero Division")
        except OverflowError:
            print(" !! Error !! - To over much number ")
    else:
        print("  Choose Operator from 1 - 5 ")
    loop = input("  Press Any Key to try again. Press 'n' to quit: ")
    calc_loop = True if loop != "n" else False
################################################################################################
print(" End Calculator ")
