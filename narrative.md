****Abstract****

This project compares artificial intelligence generated content labels for a set of images against identically generated labels for reduced resolution versions of those same images.


<br>

****Introduction****

The Google Vision artificial intelligence (AI), like most AIs, is opaque and the labels it assigns are based on unknown machine learning image sets. Yet AIs are becoming an increasingly significant audience, the machine gaze used to evaluate us, for instance, as potential consumers — or potential threats. In this project, I turn Google Vision's AI gaze on the official New York City presentation of self through the Instagram social media channel. In keeping with the spirit of Data TRIKE, I investigate here how the manipulation of data inputs (in this case image resolution) affects the AI's interpretation of the image contents.

I chose the NYC instagram account to lay ground work and test methods for a potential future project which would use artificial intelligence content labeling on a more extensive set of governmental social media images.

I chose Google Vision due to the accessibility of its API, which includes a test function where one can get sample results on a single image at a time without coding. After initial testing I wrote code, based on sample code provided in the documentation, to pull results for batches of images.


<br>

****Base dataset****

The base dataset is comprised of 387 images downloaded on March 2, 2019 from the official New York City Instagram account at https://www.instagram.com/nycgov/. This is the top-level social media account featured on https://www1.nyc.gov/connect/social-media.page (as of 3/2/19).

To obtain the images I used a Chrome extension called "Downloader for Instagram™ (+ Upload photo)" version 5.0.70, offered by developer aboveradiant@gmail.com. 

Critique: I do not have insight into the inner workings of this plug-in. It downloaded images of varying dimensions, which is consistent with the different maximum resolutions allowed on Instagram at different times. I spot checked the dimensions of a sample of downloaded images against the dimensions listed under "Inspect Element" in the Safari browser when viewing the Instagram page and found that the "natural" dimensions listed were consistent with the dimensions of the images as downloaded.

LINK TO DATA: https://github.com/HannimalCrackers/MALS75500/tree/master/01_image-sets/NYC


<br>

****Transform stage 1****

Transform stage 1: create second test image set at reduced resolution

I created an action in Photoshop that reduced images to 50% original dimensions using the Image Size function in Photoshop, constraining the dimensions and using automatic resampling, and then saved the down-resolutioned images as maximum-quality JPEGs (standard baseline). I ran this action twice, resulting in images that were 25% the original dimensions (e.g., a 1080 × 1349 px image was reduced to 270 × 338 px).

Critique: In retrospect I should have run a single action that saved down to 25% in one step, as JPEG is a lossy compression format and introducing an extra level of saving as a JPEG could potentially introduce compression artifacts that might influence the Google Vision artificial intelligence's interpretation of the image contents.

LINK TO DATA: https://github.com/HannimalCrackers/MALS75500/tree/master/01_image-sets/NYC_25pct


<br>

****Transform stage 2****

Transform stage 2: artifical intelligence content labels using API

I wrote a Python script, based off samples provided in the Google Vision API documentation, that runs all of the images in the same folder as the script through the Google Vision API and pulls content labels for each image. I ran this script on both the base set of full-size images and on the reduced size set of images. The output of the script is a CSV with each result for each image on a separate line.


Critique: As stated in the introduction, I went into this project fully aware that the Google Vision AI is opaque and the labels assigned are based on unknown machine learning image sets. The watchout here is to keep in mind that the AI is not providing a determination of image contents, but rather an interpretation – the foundations of which are unknowable. One potential point of weakness in the data flow at this stage is in the Python script used to interact with the Google Vision API. My script seems to be interacting with the AI as desired, but code is an easy place for undesired functionality to slip in, particularly with less experienced coders.

LINK TO DATA - THIS HAS TWO SCRIPTS AND TWO OUTPUT CSVS:

NYC Script: https://github.com/HannimalCrackers/MALS75500/blob/master/02_script/NYC/label-getter_nyc.py
NYC Output CSV: https://github.com/HannimalCrackers/MALS75500/blob/master/03_script-output/NYC/stage1_out_nyc.csv

NYC 25% Script: https://github.com/HannimalCrackers/MALS75500/blob/master/02_script/NYC_25pct/label-getter_nyc_25pct.py
NYC 25% Output CSV: uploaded wrong file, replace

<br>

****Transform stage 3****

Transform stage 3: manipulating the data formatting

I would have liked to write a Python script to accomplish the following, but ended up just using Excel to save time. In this stage I edited the CSV output of my Python script from stage 2. I deleted all brackets, single quotes, and spaces after commas, added a column with the cityname, added column headers (field names), and saved as a CSV.

Critique: Any manual intervention like this is subject to errors of consistency. I did use global functions such as "Find and Replace" to minimize the likelihood of such.

LINK TO DATA - THIS HAS TWO CSVS:

NYC:
NYC 25%: 


<br>

****Analysis****

The quantitative reduction in image resolution resulted in a qualitative difference in the recognized content.


<br>

****Fair use****

It is my belief that hosting a copy of the base Instagram image set in a zip on a GitHub repository linked to the Data TRIKE website is in accordance with fair use. The purpose of hosting the base dataset alongside the data transformations is to provide an educational example of the choices made in collecting and working with the data. Hosting these images in zip form will not divert viewers away from the @nycgov Instagram account.
