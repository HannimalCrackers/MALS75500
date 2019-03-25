****Abstract****

This project compares artificial intelligence generated content labels for a set of images against identically generated labels for reduced resolution versions of those same images.


<br>

****Introduction****

Why the NYC instagram account...

This is laying the ground work and testing methods for a potential future project which would use artificial intelligence content labeling on a more extensive set of governmental social media images.

Why Google Vision...


<br>

****Base dataset****

The base dataset is comprised of 387 images downloaded on March 2, 2019 from the official New York City Instagram account at https://www.instagram.com/nycgov/. This is the top-level social media account featured on https://www1.nyc.gov/connect/social-media.page (as of 3/2/19).

To obtain the images I used a Chrome extension called "Downloader for Instagram™ (+ Upload photo)" version 5.0.70, offered by developer aboveradiant@gmail.com. 

Critique: I do not have insight into the inner workings of this plug-in. It downloaded images of varying dimensions, which is consistent with the different maximum resolutions allowed on Instagram at different times. I spot checked the dimensions of a sample of downloaded images against the dimensions listed under "Inspect Element" in the Safari browser when viewing the Instagram page and found that the "natural" dimensions listed were consistent with the dimensions of the images as downloaded.

LINK TO DATA:


<br>

****Transform stage 1****

Transform stage 1: create second test image set at reduced resolution

I created an action in Photoshop that reduced images to 50% original dimensions using the Image Size function in Photoshop, constraining the dimensions and using automatic resampling, and then saved the down-resolutioned images as maximum-quality JPEGs (standard baseline). I ran this action twice, resulting in images that were 25% the original dimensions (e.g., a 1080 × 1349 px image was reduced to 270 × 338 px).

Critique: In retrospect I should have run a single action that saved down to 25% in one step, as JPEG is a lossy compression format and introducing an extra level of saving as a JPEG could potentially introduce compression artifacts that might influence the Google Vision artificial intelligence's interpretation of the image contents.

LINK TO DATA:


<br>

****Transform stage 2****

Transform stage 2: artifical intelligence content labels using API

I wrote a Python script, based off samples provided in the Google Vision API documentation, that runs all of the images in the same folder as the script through the Google Vision API and pulls content labels for each image. I ran this script on both the base set of full-size images and on the reduced size set of images. The output of the script is a CSV with each result for each image on a separate line.


Critique:

LINK TO DATA - THIS HAS TWO SECTIONS:



<br>

****Transform stage 3****

Transform stage 3: manipulating the data formatting

- Ideally this would have been done in Python as well but I worked in Excel to save time
- Deleted all brackets, single quotes, spaces after commas
- Added column with cityname
- Added column headers
- Saved out as CSV


Critique: 

LINK TO DATA - THIS HAS TWO SECTIONS:



<br>

****Analysis****

Lorem ipsum


<br>

****Fair use****

It is my belief that hosting a copy of the base Instagram image set in a zip on a GitHub repository linked to the Data TRIKE website is in accordance with fair use. The purpose of hosting the base dataset alongside the data transformations is to provide an educational example of the choices made in collecting and working with the data. Hosting these images in zip form will not divert viewers away from the @nycgov Instagram account.
