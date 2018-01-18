import sys
import tensorflow as tf
        
flags = tf.app.flags
flags.DEFINE_string(flag_name='colour',
                    default_value='green',
                    docstring='the colour to make a flower')

def main():
    flags.FLAGS._parse_flags(args=sys.argv[1:])
    print('a {} flower'.format(flags.FLAGS.colour))

if __name__ == '__main__':
    main()