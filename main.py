import sys

from to_try import get_district


def main():
    # Берём адрес из командной строки
    toponym_to_find = ' '.join(sys.argv[1:])
    if toponym_to_find:
        result = get_district(toponym_to_find)
        print(result)
    else:
        print('Nop')


if __name__ == '__main__':
    main()
