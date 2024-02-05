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
    for dict_ in data:
        new_dicts = {}
        for k, v in dict_.items():
            if k == 'date':
                result = re.sub('T', ' ', v)
                result = datetime.datetime.strptime(result, '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y')
                dict_[k] = result
                new_dicts.update(dict_)
            else:
                new_dicts.update(dict_)
        date_fix.append(new_dicts)
    return date_fix


def hide_data_payment():

    date_fix = []
    data = format_date()
    for dict_ in data:
        for k, v in dict_.items():
            #print(k, v)
            try:
                if 'Счет' in v:
                    split_str = v.split(' ')
                    words = split_str[0:-1]
                    hided = split_str[-1]
                    #print(split_str)
                    hided_digits = '*' * 2 + hided[-4:]
                    sum_words = ' '.join(words)
                    result = sum_words + ' ' + hided_digits
                    dict_[k] = result
                elif 'Visa' or 'Maestro' or 'MasterCard' in v:
                    continue
            except:
                continue


        date_fix.append(dict_)
    #return date_fix
    print(date_fix)

hide_data_payment()
#print(format_date())
