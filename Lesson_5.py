new_result = []
new_str_1 = '0123456789'
for stm_1 in new_str_1:
    for stm_2 in new_str_1:
        result = stm_1 + stm_2
        if result.isalnum():
            result = int(result)
            new_result.append(result)
            # print(result)
print(new_result)

