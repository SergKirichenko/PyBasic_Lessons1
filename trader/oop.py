from argparse import ArgumentParser
from typing import Union  # , List, Dict
import json
import os.path
import csv
import datetime
import random


##################################################################################################################
class Trader:
    path_logs = "logs.csv"
    path_file_stat = "config_status.json"
    start_file = "config.json"

    def __init__(self, path_logs=path_logs, path_file_stat=path_file_stat, start_file=start_file):
        self.start_file = start_file
        self.path_logs = os.path.join(path_logs)
        self.path_file_stat = os.path.join(path_file_stat)
        self.data = self.read_json_file(self.path_file_stat)
        self.rate, self.money_uah, self.money_usd, self.delta = self.read_data_dict()
        self.data_logs, self.data_list = self.stat_logs_update()

    def read_json_file(self, path_file) -> dict:
        with open(path_file, 'r') as file:
            self.data = json.load(file)
        return self.data

    def read_data_dict(self):
        self.rate = self.data["rate"]
        self.money_usd = self.data["amount on account USD"]
        self.money_uah = self.data["amount on account UAH"]
        self.delta = self.data["delta"]
        return [self.rate, self.money_uah, self.money_usd, self.delta]

    def update_data_dict(self) -> dict:
        self.data["rate"] = self.rate
        self.data["amount on account USD"] = round(self.money_usd, 2)
        self.data["amount on account UAH"] = round(self.money_uah, 2)
        self.data["delta"] = self.delta
        return self.data

    def write_json_file(self, new_data) -> None:
        with open(self.path_file_stat, 'w') as file:
            json.dump(new_data, file, indent=2)

    ##############################################################################################
    def logs_read(self) -> Union[list, int]:
        data = []
        with open(self.path_logs, 'r', newline='') as file:
            reader = csv.reader(file, delimiter='|')
            nom = 0
            for row in reader:
                data.append(row)
                nom += 1
        return [data, nom]

    def stat_logs_update(self):
        date_time = datetime.datetime.now().strftime("%d-%m-%y %X")
        self.data_list, nom = self.logs_read()
        self.data_logs = [nom, self.rate, self.delta, self.money_usd, self.money_uah, date_time]
        return self.data_logs, self.data_list

    def logs_write(self, data_logs):
        with open(self.path_logs, 'a', newline='') as file:
            csv.writer(file, delimiter='|').writerow(data_logs)

    ######################################################################################################
    # Ф-ция Заново
    def reset_file(self):
        data = self.read_json_file(self.start_file)
        self.write_json_file(new_data=data)
        header = self.data_list[0]
        with open(self.path_logs, 'w', newline='') as file:
            csv.writer(file, delimiter='|').writerow(header)

    # Ф-ция Инфо для счетов
    def available_info(self) -> None:
        print(f"USD {round(self.money_usd, 2)} UAH {round(self.money_uah, 2)}")

    # Ф-ция Инфо Курса валюты
    def rate_val(self) -> None:
        print(f"{self.rate}")

    ###################################################
    def update_write(self):
        new_data = self.update_data_dict()
        self.write_json_file(new_data=new_data)
        self.stat_logs_update()
        self.logs_write(self.data_logs)

    # Алгоритм NEXT
    def next_rate(self):
        delta_range = random.triangular(-0.5, 0.5, 0.01)
        self.rate = round((self.rate + delta_range), 2)
        self.delta = round(delta_range, 2)
        self.update_write()

    # ф-ция покупки n-го кол-ва валюты
    def buy_usd(self, input_buy: float, ):
        deal = input_buy * self.rate
        if (self.money_uah - deal) > 0:
            self.money_uah -= round(deal, 2)
            self.money_usd += input_buy
            self.update_write()
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH: {round(deal, 2)}, AVAILABLE {round(self.money_uah, 2)}")

    # Покупка ВСЁ
    def buy_all(self):
        deal = self.money_uah / self.rate
        self.money_usd += round(deal, 2)
        self.money_uah -= round((deal * self.rate), 2)
        self.update_write()

    # Ф-ция продажи кол-ва USD
    def sell_usd(self, input_sell: float):
        if input_sell <= self.money_usd:
            deal = input_sell * self.rate
            self.money_uah += round(deal, 2)
            self.money_usd -= round(input_sell, 2)
            self.update_write()
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD: {round(input_sell, 2)}, AVAILABLE {round(self.money_usd, 2)}")

    #  Ф-ция Продажа На ВСЕ
    def sell_all(self):
        deal = self.money_usd * self.rate
        self.money_uah += round(deal, 2)
        self.money_usd -= round((deal / self.rate), 2)
        self.update_write()


#####################################################################################################################
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

###################################################################################################################
trader = Trader()
commands = {'NEXT': trader.next_rate,
            'RATE': trader.rate_val,
            'AVAILABLE': trader.available_info,
            'BUY': trader.buy_usd,
            'SELL': trader.sell_usd,
            'RESTART': trader.reset_file,
            'BUY ALL': trader.buy_all,
            'SELL ALL': trader.sell_all,
            }
#####################################################################################################################
# Запуск сценариев
if keys in ("NEXT", "RATE", "AVAILABLE", "BUY ALL", "SELL ALL", "RESTART"):
    play_sc = commands[keys]
    play_sc()
else:
    play_sc = commands[keys]
    play_sc(score)
################################################################################################################
# The End
