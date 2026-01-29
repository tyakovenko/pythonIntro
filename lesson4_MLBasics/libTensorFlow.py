"----------------------------------------------------------------------------"
"----- Extra example using tensor flow--------------- ignore for now but can use for performance----"
import tensorflow as tf
from tensorflow.keras import layers
tf_model = tf.keras.Sequential([
    layers.Dense(units=1, input_shape=[1])
])

# 2. Configure how it learns
tf_model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
    loss='mean_squared_error'
)

# 3. Train (Epochs = how many times it looks at the data)
history = tf_model.fit(X_train, y_train, epochs=20, verbose=0)

# 4. Predict
tf_predictions = tf_model.predict(X_test)