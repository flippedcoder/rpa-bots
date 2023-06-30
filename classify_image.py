import numpy as np
import pandas as pd

from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image

model = VGG16(weights="imagenet")

# image loaded in PIL (Python Imaging Library)
img = image.load_img('../Example_Data/unlabeled_image.jpg', color_mode="rgb", target_size=(224, 224))

# Converts a PIL Image to 3D Numpy Array
x = image.img_to_array(img)

# Adding the fouth dimension, for number of images
x = np.expand_dims(x, axis=0)

x = preprocess_input(x)

features = model.predict(x)

predictions = decode_predictions(features)[0]
predictions.sort(key=lambda x: x[2])

predicted_classification = predictions[-1][1]