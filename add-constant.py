import tensorflow as tf

v1 = tf.Variable([1,2,3,4])
v2 = tf.Variable([5,4,3,2])

add = tf.add(v1+v2)

with tf.Session() as sess:
    print(sess.run(add))