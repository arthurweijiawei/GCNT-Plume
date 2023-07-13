#    Author: Ankit Kariryaa, University of Bremen

import tensorflow as tf
from tensorflow.keras.optimizers import Adam, Adadelta, Adagrad, Nadam

# Optimezers; https://keras.io/optimizers/
adaDelta = Adadelta(learning_rate=1.0, rho=0.95, epsilon=None, decay=0.0)
adam = Adam(learning_rate=0.001, beta_1= 0.9, beta_2= 0.999, epsilon= 1.0e-8)#5.0e-05 decay= 0.0, 
nadam = Nadam(learning_rate=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004)
adagrad = Adagrad(learning_rate=0.01, epsilon=None, decay=0.0)

adaDelta = tf.keras.mixed_precision.LossScaleOptimizer(adaDelta)
adam = tf.keras.mixed_precision.LossScaleOptimizer(adam)
nadam = tf.keras.mixed_precision.LossScaleOptimizer(nadam)
adagrad = tf.keras.mixed_precision.LossScaleOptimizer(adagrad)