import sys


def add_one(number):
    return number + 1

def main():
    print("This is the name of the program:", sys.argv[0])
    print("Argument List:", str(sys.argv))
    try:
        print(add_one(int(sys.argv[1])))
    except IndexError as err:
        print('No index: ', err)


if __name__ == "__main__":
    main()