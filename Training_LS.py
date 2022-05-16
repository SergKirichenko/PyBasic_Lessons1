import random


#####################################################################################################################
# Функция Изменения Курса Валюты
def trade_area(rate_usd):
    range_list = []
    for i in range(0, 20):
        range_list.append(random.randint(-50, 50))
    random.shuffle(range_list)
    delta1 = random.choice(range_list)
    delta2 = random.choice(range_list)
    delta3 = random.choice(range_list)
    delta4 = random.choice(range_list)
    delta = ((delta1 + delta2 + delta3 + delta4) // 4) / 100
    rate_usd = rate_usd + delta

    return round(rate_usd, 2)


