import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import pathlib

os.chdir('C:/Users/Kyle Brown/Desktop/CWU/Year 3/Quarter 2/CS481/TRAIN_ZONE/')

print('Loading model...')
model = keras.models.load_model('buggyAI_V4.1.h5')
print('Model loaded successfully')

img_height = 180
img_width = 180

class_names = ['Aphids', 'Cicadellidae', 'Lycorma_Delicatula', 'Miridae', 'None']

img_name = 'spottedlanternfly4.png'
test_data = 'D:\\Testing\Examples\\' + img_name
test_dir = pathlib.Path(test_data)

img = keras.preprocessing.image.load_img(
    test_dir, target_size=(img_height, img_width)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)
print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

print("donezoooo")


