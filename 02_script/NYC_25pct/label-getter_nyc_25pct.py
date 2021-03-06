import csv
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()
 
# Creates csv for results to be written into
# CSV name manually changed in script for each city image set
with open('stage1_out_nyc_25pct.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)

    # Path to directory with images, must be same folder as script
    # Need to manually change path for each city image set
    for file in os.listdir('/Users/hhouse/Projects/GoogleVision/VirtualEnv/env/image-sets/NYC_25pct'):
        if file.endswith(".jpg"):

        # Loads the image into memory
            with io.open(file, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)

            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

            # Make list of each label result and write to csv
            for label in labels:
                list = [file, label.description, label.score, label.mid]              
                writer.writerow([list])

