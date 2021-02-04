import sys
from functions import log, show, take_survey

def main():
    args = sys.argv[1:]

    if (args[0] == "log"):
        log()

    elif (args[0] == "show"):
        if (len(args) == 1):
            show()

if __name__ == '__main__':
    main()
