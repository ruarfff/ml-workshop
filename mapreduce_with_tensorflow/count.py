from __future__ import print_function

import time
import tensorflow as tf

# RunConfig automatically reads the TF_CONFIG enviroonment variable we set earlier
config = tf.contrib.learn.RunConfig()

# We start a server
# cluster_spec has info about all other jobs in the cluster
# The servers job name is taken from the config under task.type
# The task index is taken form task.index (index is based on task types so is only greater than 0 when more of the same task type exists)
server = tf.train.Server(config.cluster_spec,
                         job_name=config.task_type,
                         task_index=config.task_id)
# We start a sesion that waits for the rest of the cluster to join
session = tf.Session(server.target)

# Runs on all machines
# The next line says the queue should only live on the file machine but be availale everywhere.
# /job:files/task:0 addresses the job configure with the type 'files' and index 0
with tf.device('/job:files/task:0'):
    filename_queue = tf.FIFOQueue(capacity=10, dtypes=[tf.string],
                                  shared_name='filename_queue')

# Runs only on file machine
# Creates and populates the file queue
if config.task_type == 'files':
    filename_to_enqueue = tf.placeholder(tf.string)
    enqueue_filename = filename_queue.enqueue(filename_to_enqueue)
    close_filename_queue = filename_queue.close()
    for line in open('filenames.txt', encoding="utf8"):
        filename = line.strip()
        session.run(enqueue_filename,
                    feed_dict={filename_to_enqueue: filename})
    session.run(close_filename_queue)
    server.join()

# Runs on all machines. Availabe on all machines but only exists in the reducer.
with tf.device('/job:reduce/task:0'):
    total_word_count = tf.Variable(0, name='total')

# Runs only on reducer machines
if config.task_type == 'reduce':
    initializer = tf.global_variables_initializer()
    session.run(initializer)
    while True:
        total_word_count_now = session.run(total_word_count)
        print('{} words so far'.format(total_word_count_now))
        time.sleep(2)

# Runs only on mapper machines
if config.task_type == 'map':
    filename_from_queue = filename_queue.dequeue()
    word_count_to_add = tf.placeholder(tf.int32)
    add_to_total = tf.assign_add(total_word_count,
                                 word_count_to_add,
                                 use_locking=True)
    while True:
        filename = session.run(filename_from_queue)
        text = open(filename, encoding="utf8").read()
        # Note, this is just regular python code calculating the count
        this_word_count = len(text.split())
        # This work is done off the graph and then pushed on the the graph
        time.sleep(3)
        print('{} words in {}'.format(this_word_count, filename))
        # Because add_to_total has a reference to total_word_count, it adds the total in the reducers memory. TensorFlow handles all that complexity. 
        session.run(add_to_total,
                    feed_dict={word_count_to_add: this_word_count})
