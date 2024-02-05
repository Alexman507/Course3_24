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
    date_filtered = []
    data = get_data()
    for d in data:
        if d.get('state') == 'EXECUTED' and d.get('date'):
            date_filtered.append(d)
    return date_filtered


def sorted_data():
    data = correct_date()
    data = sorted(data, key=lambda x: x.get('date'), reverse=True)
    return data


def get_date(x, format="%Y-%m-%d %H:%M:%S.%f"):
    return dt.strptime(x.get("date"), format)


print(correct_date())
