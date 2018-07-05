import tensorflow as tf
import numpy as np

import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as pl


num_point = 1000
vector_set = []

for i in range(num_point):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.00, 0.03)
    # y1 = np.random.normal(4.00, 0.2)
    vector_set.append([x1, y1])

x_data = [v[0] for v in vector_set]
y_data = [v[1] for v in vector_set]

pl.plot(x_data, y_data, "ro")
pl.legend()
pl.show()

a = tf.placeholder("float")
b = tf.placeholder("float")

y = tf.multiply(a, b)

sess = tf.Session()

print(sess.run (y, feed_dict={a:3, b:5}))