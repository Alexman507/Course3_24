import json
from datetime import datetime as dt


def get_data():
    with open('data/operations.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
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


def get_date():
    x = sorted_data()
    return dt.strptime(x.get("date"), format="%Y-%m-%d %H:%M:%S.%f")


print(sorted_data())
