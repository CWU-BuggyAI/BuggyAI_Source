from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import numpy as np
import pathlib

app = Flask(__name__)
CORS(app)

# Loading the ML model
print("Loading ML Model")
model = load_model('models/buggyAI_V4.1.h5')

@app.route('/prediction', methods=["POST"])
def pred():
    print('[----- Buggy AI (POST) -----]')

    imgFile = request.files['file']
    img = Image.open(imgFile)
    img = np.asarray(img.resize((180, 180)))

    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    class_names = ['Aphids', 'Cicadellidae', 'Lycorma_Delicatula', 'Miridae', 'None']

    pred = model.predict(img_array)
    score = tf.nn.softmax(pred[0])

    prediction = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)], 100 * np.max(score))
    return jsonify(prediction)

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/About.html', methods=["GET"])
def about():
    return render_template('About.html')

@app.route('/Manual.html', methods=["GET"])
def manual():
    return render_template('Manual.html')
