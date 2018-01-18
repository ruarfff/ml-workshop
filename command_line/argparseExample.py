import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--colour',
                    default='green',
                    help='the colour to make the flower')

def main():
    args = parser.parse_args(sys.argv[1:])
    print('a {} flower'.format(args.colour))

if __name__ == '__main__':
    main()