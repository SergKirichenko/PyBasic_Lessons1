#################################################################
my_list = [25, 43, 14, 134, -73, 523, 84, 472, 293, 5, ]
# my_list = [15, 12, 100, ]

for item in my_list:
    if item > 100:
        print(item)
##################################################################

my_result = []
for item in my_list:
    if item > 100:
        my_result.append(item)
print(my_result)

##################################################################

if len(my_list) <= 2:
    result = 0
else:
    result = my_list[-1] + my_list[-2]

my_list.append(result)
print(my_list)

########################### второй вариант через тернарный оператор
#####################################################################
# result = 0 if len(my_list) <= 2 else my_list[-1] + my_list[-2]
# my_list.append(result)
# print(my_list)
