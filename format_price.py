import sys


def format_price(price):
    if isinstance(price, float):
        int_number = int(price)
        pretty_number ='{0:,}'.format(int_number).replace(',', ' ')
        return pretty_number
    else:
        try:
            int_number = int(price)
            print(int_number)
            pretty_number = '{0:,}'.format(int_number).replace(',', ' ')
        except IndexError:
            print('error')
    return pretty_number


def main():
    price_to_format = sys.argv[0]
    print(price_to_format)
    print(format_price(price_to_format))


if __name__ == '__main__':
    main()
