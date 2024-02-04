import json
from datetime import datetime as dt
import re


def get_data():
    with open('data/operations.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


def get_dumps():
    data = json.dumps(get_data(), ensure_ascii=False, sort_keys=True, indent=4)
    return data


def correct_date():
    d = get_dumps()
    d = (i) for i in d.replace('T', ' ')


def get_date(x, format="%Y-%m-%d" + "T" + "%H:%M:%S.%f"):
    return dt.strptime(x.get("date"), format)


def sorted_data():
    data = get_data()
    data = sorted(data, key=get_date, reverse=True)
    return data


print(get_dumps())
