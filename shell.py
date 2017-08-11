import core, disk, random, time, sys


def input_choice(number, string):
    while True:
        choice = input(string).strip()
        if choice.lower() == 'q':
            sys.exit()
        for i in range(1, number):
            if choice == str(i):
                return choice
        else:
            print(
                '----------------',
                '\n!Invalid Input!\n',
                '----------------',
                sep='')


def main():
    start = ''
    while start != 'q':
        item_dictionary = disk.open_item_dictionary()
        print(item_dictionary)
        start = 'q'


if __name__ == '__main__':
    main()