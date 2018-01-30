import tensorflow as tf

message = tf.constant("hello World")

with tf.Session() as sess:
    print(sess.run(message).decode())