import utils

if __name__ == '__main__':
    data = utils.body_payment_data()
    for payment in data:
        print(
            payment.get('date'),
            payment.get('description'),
            '\n',
            payment.get('from'),
            '->',
            payment.get('to'),
            '\n',
            payment.get('amount'),
            payment.get('name'),
            '\n',
            end='\n',
        )
