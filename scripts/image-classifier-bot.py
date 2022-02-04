import requests
import pandas as pd
import yagmail
import wget
import shutil

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


# run through model to determine what it is

# move image to correct folder with appropriate label

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
