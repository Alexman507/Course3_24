import datetime
import json
import re


def get_data():
    with open('data/operations.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


def filter_date():
    date_filtered = []
    data = get_data()
    for d in data:
        if d.get('state') == 'EXECUTED' and d.get('date'):
            date_filtered.append(d)
    return date_filtered


def sorted_date():
    data = filter_date()
    data = sorted(data, key=lambda x: x.get('date'), reverse=True)
    return data


def format_date():
    date_fix = []
    data = sorted_date()
    for dicts in data:
        new_dicts = {}
        for k, v in dicts.items():
            if k == 'date':
                result = re.sub('T', ' ', v)
                result = datetime.datetime.strptime(result, '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y')
                dicts[k] = result
                new_dicts.update(dicts)
            else:
                new_dicts.update(dicts)
        date_fix.append(new_dicts)
    return date_fix

