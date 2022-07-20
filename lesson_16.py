# полиморфизм
import json
import re


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def sort_by_name(math_dict):
    return math_dict["name"].split()[-1]


def sort_by_text(math_dict):
    return len(math_dict["text"].split())


def sort_by_bday(math_dict):
    years = math_dict["years"]
    # pattern = r'\d+'  #[0-9] [a-z]  [A-Z] [A-Za-z] [А-Я] [А-ЯІЇҐ] \d \w  [0-9]{3}
    years = re.findall(r'\d+', years)
    bday = int(years[0]) if "BC" not in math_dict["years"] else - int(years[0])
    return bday, math_dict["name"].split()[-1]


data = read_json('math.json')

# sorted_data = sorted(data, key=lambda x: len(x["text"].split()))

sorted_data = sorted(data, key=sort_by_bday)

print(sorted_data)





# my_list = [1, -3, 14, -7]
# s_list = sorted(my_list, key=abs)
# print(s_list)

# my_list = ["55555", "aaa", "qqqq", "AAAAAAAAAAAAAA"]
# s_list = sorted(my_list, key=len)
# print(s_list)



# class BBox:
#     def __init__(self, x0, y0, x1, y1):
#         self._x0 = x0
#         self._y0 = y0
#         self._x1 = x1
#         self._y1 = y1
#
#     def __repr__(self):
#         return f"({self._x0};{self._y0})-({self._x1};{self._y1})"
#
#     def get_area(self):
#         return (self._x1 - self._x0) * (self._y1 - self._y0)
#
#     def __add__(self, other):
#         new_x0 = min(self._x0, other._x0)
#         new_y0 = min(self._y0, other._y0)
#         new_x1 = max(self._x1, other._x1)
#         new_y1 = max(self._y1, other._y1)
#         return BBox(new_x0, new_y0, new_x1, new_y1)
#
#     def __gt__(self, other):
#         area_1 = self.get_area()
#         area_2 = other.get_area()
#         return area_1 > area_2
#
#
#
# bbox_1 = BBox(0, 0, 3, 6)
# bbox_2 = BBox(1, 2, 5, 5)
#
# bbox_list = [bbox_1, bbox_2]
#
# bbox_3 = bbox_1 > bbox_2
#
# print(sorted(bbox_list, reverse=True))













# val_1 = 1.2
# val_2 = 2.3
# result = val_1 + val_2
# print(result)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
