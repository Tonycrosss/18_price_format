def format_price(price):
    if isinstance(price, float):
        int_number = int(price)
        pretty_number ='{0:,}'.format(int_number).replace(',', ' ')
    return pretty_number


def main():
    format_price('3334.2442')


if __name__ == '__main__':
    main()
