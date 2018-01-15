import tensorflow as tf

def main(args):
    assert args[1] == '--colour'
    print('a {} flower'.format(args[2]))

if __name__ == '__main__':
    tf.app.run()