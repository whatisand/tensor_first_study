import tensorflow as tf
import matplotlib.pyplot as plt

x_data = [1, 2, 3]
y_data = [1, 2, 3]

# W = tf.placeholder(tf.float32)
W = tf.Variable(tf.random_normal([1]), name='weight')
# W = tf.Variable(-34.0)
# X = tf.placeholder(tf.float32)
# Y = tf.placeholder(tf.float32)

hypothesis = x_data * W

# cost = tf.reduce_mean(tf.square(hypothesis - Y))
cost = tf.reduce_mean(tf.square(hypothesis - y_data))

learning_rate = 0.1

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)
# gradient = tf.reduce_mean((W * X - Y) * X)
# descent = W - learning_rate * gradient

# update_W = W.assign(descent)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

W_val = []
cost_val = []
print(sess.run(W))
for i in range(10):
    # print(i, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))
    # sess.run(update_W, feed_dict={X: x_data, Y:y_data})
    curr_W = sess.run(W)
    cost_val.append(sess.run(cost))
    print(i, curr_W)
    W_val.append(curr_W)
    sess.run(train)

plt.plot([i for i in range(10)], W_val)
plt.show()
plt.plot([i for i in range(10)], cost_val)
plt.show()
