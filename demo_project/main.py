from utils import log
from config import InvalidValueError, BalanceError
from service import check_amount

def main():
    try:
        amount = int(input('Nhập amount: '))
        balance = int(input('Nhập balance: '))
        check_amount(amount, balance)

    except InvalidValueError as e:
        log(e)
    except BalanceError as e:
        log(e)
    except ValueError:
        log('Bạn phải nhập số')

if __name__ == '__main__':
    main()