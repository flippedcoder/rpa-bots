import requests
import pandas as pd
import yagmail
import shutil

from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np

# get new image from Cloudinary
image_url = "https://res.cloudinary.com/milecia/image/upload/v1625834860/test0/fmgidql8t2id8wxomghl.png"
filename = image_url.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream=True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True

    # Open a local file with wb ( write binary ) permission.
    with open(filename, "wb") as f:
        shutil.copyfileobj(r.raw, f)

    print("Image sucessfully downloaded: ", filename)
else:
    print("Image could not be retreived")


model = VGG16(weights="imagenet")

# image loaded in PIL (Python Imaging Library)
img = image.load_img(filename, color_mode="rgb", target_size=(224, 224))

# Converts a PIL Image to 3D Numpy Array
x = image.img_to_array(img)

# Adding the fouth dimension, for number of images
x = np.expand_dims(x, axis=0)

x = preprocess_input(x)

features = model.predict(x)

predictions = decode_predictions(features)[0]
predictions.sort(key=lambda x: x[2])

predicted_classification = predictions[-1][1]

# move image to correct folder with appropriate label
if predicted_classification == True:
    shutil.move(filename, "rejected")
else:
    shutil.move(filename, "accepted")

# send email about unidentified images
receiver = "test@gmail.com"
body = "See if you can figure out what these images are. The model missed them."
filename = "f{filename}.png"

yag = yagmail.SMTP("my@gmail.com")
yag.send(
    to=receiver,
    subject="Unlabeled images",
    contents=body,
    attachments=filename,
)
