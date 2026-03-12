from config import InvalidValueError, BalanceError, max_balance

def check_amount(amount, balance):
    if amount <= 0 or balance <= 0:
        raise InvalidValueError('amount và balance phải > 0')

    if balance > max_balance:
        raise InvalidValueError('balance vượt quá giới hạn')

    if amount > balance:
        raise BalanceError('amount không được lớn hơn balance')

    print('Hợp lệ')