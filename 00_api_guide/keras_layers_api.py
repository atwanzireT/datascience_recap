from tensorflow.keras import layers
from tensorflow as tf

layer = layers.Dense(32, activation = "relu")
inputs = tf.random.uniform()