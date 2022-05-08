from argparse import ArgumentParser
from typing import Union, List, Dict
import json
import csv
import os
import datetime
import random

args = ArgumentParser()
args.add_argument("command", type=str)
args.add_argument("second", nargs="?", default="")
args = vars(args.parse_args())
key = args['command'].upper()
sub_key = args['second']
score = 0
if sub_key.isalpha():
    keys = f"{key} {sub_key.upper()}"
elif sub_key.isdigit():
    keys = key
    try:
        score = float(sub_key)
    except TypeError:
        print("Enter correct number!")
else:
    keys = key


#####################################################################################################################
# Ф-ции чтения и записи файл-статуса
def read_json_file(filename_) -> Union[Dict]:
    with open(filename_, 'r') as file:
        data = json.load(file)
    return data


def write_json_file(data: Union[List, Dict], filename_: str = "config_logs.json") -> None:
    with open(filename_, 'w') as file:
        json.dump(data, file, indent=2)


####################################################################################################################
# Ф-ции записи логов
def stat_logos(rate_: float = 0, delta_: float = 0, money_usd_: float = 0, money_uah_: float = 0, clear=False):
    path_file = os.path.join("logs.csv")
    date_time = datetime.datetime.now().strftime("%d-%m-%y %X")
    data = []
    with open(path_file, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='|')
        nom = 0
        for row in reader:
            data.append(row)
            nom += 1
    header = data[0]
    data_info = [nom, rate_, delta_, money_usd_, money_uah_, date_time]
    with open(path_file, 'play_sc', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(data_info)
    if clear:
        os.remove(path_file)
        with open(path_file, 'play_sc', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow(header)


#######################################################################################################################

# ф-ция покупки n-го кол-ва валюты
def buy_usd(input_buy: float, filename_: str = "config_logs.json"):
    data = read_json_file(filename_)
    rate_ = data["rate"]
    money_usd_ = data["amount on account USD"]
    money_uah_ = data["amount on account UAH"]
    deal = input_buy * rate_
    assert deal < money_uah_
    if (money_uah_ - deal) > 0:
        money_uah_ -= round(deal, 2)
        money_usd_ += input_buy
        data["amount on account USD"] = round(money_usd_, 2)
        data["amount on account UAH"] = round(money_uah_, 2)
        print(f"Deal Successful! You Buy: {input_buy},USD; Balance money: {round(money_uah_, 2)},"
              f" UAH and {round(money_usd_, 2)}, USD ")
    else:
        deal = round((money_uah_ / rate_), 2)
        print(f"Not enough money in the account. You can buy only: {deal}, USD.")

    write_json_file(data)
    stat_logos(rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_)


# Покупка ВСЁ
def buy_all(filename_: str = "config_logs.json"):
    data = read_json_file(filename_)
    rate_ = data["rate"]
    money_usd_ = data["amount on account USD"]
    money_uah_ = data["amount on account UAH"]
    deal = money_uah_ / rate_
    money_usd_ += round(deal, 2)
    money_uah_ -= round((deal * rate_), 2)
    print(f"Deal Successful! You Buy: {round(deal, 2)},USD; Balance money: {round(money_uah_, 2)},"
          f" UAH and {round(money_usd_, 2)}, USD ")
    data["amount on account USD"] = money_usd_
    data["amount on account UAH"] = money_uah_
    write_json_file(data)
    stat_logos(rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_)


# Ф-ция продажи кол-ва USD
def sell_usd(input_sell: float, filename_: str = "config_logs.json"):
    data = read_json_file(filename_)
    rate_ = data["rate"]
    money_usd_ = data["amount on account USD"]
    money_uah_ = data["amount on account UAH"]
    assert input_sell <= money_usd_
    if input_sell <= money_usd_:
        deal = input_sell * rate_
        money_uah_ += round(deal, 2)
        money_usd_ -= round(input_sell, 2)
        print(f"Deal Successful! You Sell: {input_sell},USD; Balance money: {round(money_uah_, 2)}, "
              f"UAH and {round(money_usd_, 2)}, USD ")
        data["amount on account USD"] = money_usd_
        data["amount on account UAH"] = money_uah_
    else:
        print("Input Correct Number!!!")
    write_json_file(data)
    stat_logos(rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_)


#  Ф-ция Продажа На ВСЕ
def sell_all(filename_: str = "config_logs.json"):
    data = read_json_file(filename_)
    rate_ = data["rate"]
    money_usd_ = data["amount on account USD"]
    money_uah_ = data["amount on account UAH"]
    first = data["amount on account USD"]
    deal = money_usd_ * rate_
    money_uah_ += round(deal, 2)
    money_usd_ -= round((deal / rate_), 2)
    print(f"Deal Successful! You Sell: {first},USD; Balance money: {round(money_uah_, 2)},"
          f" UAH and {round(money_usd_, 2)}, USD ")
    data["amount on account USD"] = money_usd_
    data["amount on account UAH"] = money_uah_
    write_json_file(data)
    stat_logos(rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_)


##################################################################################################################
# Ф-ция Инфо для счетов
def available_info(filename_: str = "config.json") -> None:
    dict_status = read_json_file(filename_)
    money_usd_ = dict_status["amount on account USD"]
    money_uah_ = dict_status["amount on account UAH"]
    print(f"Your Balance: on UAH account: {round(money_uah_, 2)}, UAH\n"
          f" {' ' * 13} on USD account: {round(money_usd_, 2)}, USD")


# Ф-ция Инфо Курса валюты
def rate_val(filename_: str = "config.json") -> None:
    dict_status = read_json_file(filename_)
    rate_ = dict_status["rate"]
    print(f"Now rate is: {rate_}")


# Ф-ция Заново
def reset_file(filename_: str = "config_logs.json"):
    os.remove(os.path.join(filename_))
    stat_logos(clear=True)


###################################################################################################################
# Алгоритм NEXT
def next_rate(filename_: str):
    dict_data = read_json_file(filename_)
    delta_range = random.triangular(-0.5, 0.5, 0.01)
    rate_ = dict_data["rate"]
    new_rate = round((rate_ + delta_range), 2)
    delta_ = round(delta_range, 2)
    money_usd = dict_data["amount on account USD"]
    money_uah = dict_data["amount on account UAH"]
    dict_data["rate"] = new_rate
    dict_data["delta"] = delta_
    write_json_file(dict_data)
    stat_logos(rate_=new_rate, delta_=delta_, money_usd_=money_usd, money_uah_=money_uah)


###################################################################################################################
commands = {'NEXT': next_rate,
            'RATE': rate_val,
            'AVAILABLE': available_info,
            'BUY': buy_usd,
            'SELL': sell_usd,
            'RESTART': reset_file,
            'BUY ALL': buy_all,
            'SELL ALL': sell_all,
            }
#####################################################################################################################
# Запуск сценариев
if keys in ("NEXT", "RATE", "AVAILABLE"):
    filename = "config_logs.json"
    if not os.path.isfile(os.path.join(filename)):
        filename = "config.json"
    play_sc = commands[keys]
    play_sc(filename_=filename)
elif keys in ("BUY ALL", "SELL ALL", "RESTART"):
    play_sc = commands[keys]
    play_sc()
else:
    play_sc = commands[keys]
    play_sc(score)
################################################################################################################
# The End
