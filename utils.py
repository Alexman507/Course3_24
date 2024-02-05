import datetime
import json
import re



def get_data():
    """
        Выгружает данные в состоянии "как есть"
        :return: List of dictionaries
        :rtype: list"""
    json_config = 'data/operations.json'
    with open(json_config, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


def filter_date():
    """
        Фильтрует данные, выгруженные из json файла, по ключу 'EXECUTED'
        :return: List of dictionaries
        :rtype: list"""
    date_filtered = []
    data = get_data()
    for d in data:
        if d.get('state') == 'EXECUTED' and d.get('date'):
            date_filtered.append(d)
    return date_filtered


def sorted_date():
    """
        Сортирует в списке словарей по ключу 'date' в порядке убывания
        :return: List of dictionaries
        :rtype: list"""
    data = filter_date()
    data = sorted(data, key=lambda x: x.get('date'), reverse=True)
    return data


def format_date():
    """
       Убирает из значения 'date' букву "Т", меняет формат на '%d.%m.%Y', переносит в другой список словарей
       :return: List of dictionaries
       :rtype: list"""
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
    """
       Скрывает номер счёта и номер карты (если есть)
       :return: List of dictionaries
       :rtype: list"""
    data = format_date()
    for dict_ in data:
        for k, v in dict_.items():
            # print(k, v)
            try:
                if 'Счет' in v:
                    split_str = v.split(' ')
                    words = split_str[0:-1]
                    hided = split_str[-1]
                    # print(split_str)
                    hided_digits = '*' * 2 + hided[-4:]
                    sum_words = ' '.join(words)
                    result = sum_words + ' ' + hided_digits
                    dict_[k] = result
                    continue

                if 'Visa' in v or 'Maestro' in v or 'MasterCard' in v or 'МИР' in v:
                    split_str = v.split(' ')
                    words = split_str[0:-1]
                    hided = split_str[-1]
                    # print(v)
                    hided_digits = hided[:4] + ' ' + hided[4:6] + '**' + ' ' + '****' + hided[-4:]
                    sum_words = ' '.join(words)
                    result = sum_words + ' ' + hided_digits
                    # print(result)
                    dict_[k] = result

            except:
                continue

    # print(len(data))
    return data


def slice_payment_data():
    """
       Перекладывает 5 первых словарей
       :return: List of dictionaries
       :rtype: list"""
    data = hide_data_payment()
    data_slice = data[:5]
    return data_slice


def body_payment_data():
    """
    Перекладывает переменные для вывода на экран
    :return: List of dictionaries
    :rtype: list"""
    body_data = []
    data = slice_payment_data()
    for k in data:
        # print(k)
        if k.get('from'):
            body_data.append({
                'date': k.get('date'),
                'description': k.get('description'),
                'from': k.get('from'),
                'to': k.get('to'),
                'amount': k.get('operationAmount').get('amount'),
                'name': k.get('operationAmount').get('currency').get('name'),
            })
        else:
            body_data.append({
                'date': k.get('date'),
                'description': k.get('description'),
                'from': '',
                'to': k.get('to'),
                'amount': k.get('operationAmount').get('amount'),
                'name': k.get('operationAmount').get('currency').get('name'),
            })
    return body_data


# body_payment_data()
# print(get_data())
