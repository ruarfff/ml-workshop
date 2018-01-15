# You might need to run: pip3 install python-gflags
import sys
import gflags

gflags.DEFINE_string(name='colour',
                    default='green',
                    help='the colour to make a flower')

def main():
    gflags.FLAGS(sys.argv)
    print('a {} flower'.format(gflags.FLAGS.colour))

if __name__ == '__main__':
    main()