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
key_ = args['command'].upper()
sub_key = args['second']
score = 0
if sub_key.isalpha():
    keys = f"{key_} {sub_key.upper()}"
elif sub_key.isdigit():
    keys = key_
    try:
        score = float(sub_key)
    except TypeError:
        print("Enter correct number!")
else:
    keys = key_


#####################################################################################################################
# Ф-ции чтения и записи файл-статуса
def read_json_file(filename_: str) -> dict:
    with open(filename_, 'r') as file:
        data = json.load(file)
    return data


def write_json_file(data: Union[List, Dict], filename_: str = "config_status.json") -> None:
    with open(filename_, 'w') as file:
        json.dump(data, file, indent=2)


####################################################################################################################
def logs_read(path_file) -> Union[list, int]:
    data = []
    with open(path_file, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='|')
        nom = 0
        for row in reader:
            data.append(row)
            nom += 1
    return [data, nom]


def logs_write(path_file, data_):
    with open(path_file, 'a', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(data_)


# Ф-ции записи логов
def stat_logos(rate_: float = 0, delta_: float = 0, money_usd_: float = 0, money_uah_: float = 0):
    path_file = os.path.join("logs.csv")
    date_time = datetime.datetime.now().strftime("%d-%m-%y %X")
    data_list, nom = logs_read(path_file=path_file)
    data_info = [nom, rate_, delta_, money_usd_, money_uah_, date_time]
    logs_write(path_file=path_file, data_=data_info)


def clear_logs(clear=False):
    path_file = os.path.join("logs.csv")
    data_list, nom = logs_read(path_file)
    header = data_list[0]
    if clear:
        os.remove(path_file)
        with open(path_file, 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow(header)


#######################################################################################################################
def data_read(data: dict):
    rate_ = data["rate"]
    money_usd_ = data["amount on account USD"]
    money_uah_ = data["amount on account UAH"]
    delta_ = data["delta"]
    return [rate_, money_usd_, money_uah_, delta_]


def data_write(data_: dict, rate_: float, money_usd_: float, money_uah_: float, delta: float) -> dict:
    data_["rate"] = rate_
    data_["amount on account USD"] = round(money_usd_, 2)
    data_["amount on account UAH"] = round(money_uah_, 2)
    data_["delta"] = delta
    return data_


######################################################################################################################
# ф-ция покупки n-го кол-ва валюты
def buy_usd(input_buy: float, filename_: str = "config_status.json"):
    data = read_json_file(filename_)
    rate_, money_usd_, money_uah_, delta_ = data_read(data)
    deal = input_buy * rate_
    if (money_uah_ - deal) > 0:
        money_uah_ -= round(deal, 2)
        money_usd_ += input_buy
        data = data_write(data_=data, rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_, delta=delta_)
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH: {round(deal, 2)}, AVAILABLE {round(money_uah_, 2)}")
    write_json_file(data)
    stat_logos(rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_, delta_=delta_)


# Покупка ВСЁ
def buy_all(filename_: str = "config_status.json"):
    data = read_json_file(filename_)
    rate_, money_usd_, money_uah_, delta_ = data_read(data)
    deal = money_uah_ / rate_
    money_usd_ += round(deal, 2)
    money_uah_ -= round((deal * rate_), 2)
    data = data_write(data_=data, rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_, delta=delta_)
    write_json_file(data)
    stat_logos(rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_, delta_=delta_)


# Ф-ция продажи кол-ва USD
def sell_usd(input_sell: float, filename_: str = "config_status.json"):
    data = read_json_file(filename_)
    rate_, money_usd_, money_uah_, delta_ = data_read(data)
    if input_sell <= money_usd_:
        deal = input_sell * rate_
        money_uah_ += round(deal, 2)
        money_usd_ -= round(input_sell, 2)
        data = data_write(data_=data, rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_, delta=delta_)
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE USD: {round(input_sell, 2)}, AVAILABLE {round(money_usd_, 2)}")
    write_json_file(data)
    stat_logos(rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_, delta_=delta_)


#  Ф-ция Продажа На ВСЕ
def sell_all(filename_: str = "config_status.json"):
    data = read_json_file(filename_)
    rate_, money_usd_, money_uah_, delta_ = data_read(data)
    deal = money_usd_ * rate_
    money_uah_ += round(deal, 2)
    money_usd_ -= round((deal / rate_), 2)
    data = data_write(data_=data, rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_, delta=delta_)
    write_json_file(data)
    stat_logos(rate_=rate_, money_usd_=money_usd_, money_uah_=money_uah_, delta_=delta_)


##################################################################################################################
# Ф-ция Инфо для счетов
def available_info(filename_: str = "config.json") -> None:
    dict_status = read_json_file(filename_)
    money_usd_ = dict_status["amount on account USD"]
    money_uah_ = dict_status["amount on account UAH"]
    print(f"USD {round(money_usd_, 2)} UAH {round(money_uah_, 2)}")


# Ф-ция Инфо Курса валюты
def rate_val(filename_: str = "config.json") -> None:
    dict_status = read_json_file(filename_)
    rate_ = dict_status["rate"]
    print(f"{rate_}")


# Ф-ция Заново
def reset_file():
    data = read_json_file(filename_="config.json")
    write_json_file(data=data)
    clear_logs(clear=True)


###################################################################################################################
# Алгоритм NEXT
def next_rate(filename_: str):
    data = read_json_file(filename_)
    rate_, money_usd_, money_uah_, delta_ = data_read(data)
    delta_range = random.triangular(-0.5, 0.5, 0.01)
    new_rate = round((rate_ + delta_range), 2)
    delta_ = round(delta_range, 2)
    data = data_write(data_=data, rate_=new_rate, money_usd_=money_usd_, money_uah_=money_uah_, delta=delta_)
    write_json_file(data=data)
    stat_logos(rate_=new_rate, delta_=delta_, money_usd_=money_usd_, money_uah_=money_uah_)


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
    play_sc = commands[keys]
    play_sc(filename_="config_status.json")
elif keys in ("BUY ALL", "SELL ALL", "RESTART"):
    play_sc = commands[keys]
    play_sc()
else:
    play_sc = commands[keys]
    play_sc(score)
################################################################################################################
# The End
