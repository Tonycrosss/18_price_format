import sys


def format_price(price):
    default_number = '3 245'
    try:
        int_number = int(price)
        pretty_number ='{0:,}'.format(int_number).replace(',', ' ')
        return pretty_number
    except ValueError:
        return default_number


def main():
    price_to_format = sys.argv[1]
    print(format_price(price_to_format))


if __name__ == '__main__':
    main()
