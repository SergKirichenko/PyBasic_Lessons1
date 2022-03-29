# new_result = []                           # чистый список
new_str_1 = '0123456789'
for stm_1 in new_str_1:
    for stm_2 in new_str_1:
        result = stm_1 + stm_2
        if result.isalnum():
            result = int(result)
            print(result)

            # new_result.append(result)    # можно собрать данные в список. но этого в задание не было.

# print(new_result)                        #
