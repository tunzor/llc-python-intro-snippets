# Import the pillow library; this allows us to modify images
from PIL import Image

# Image source
# https://pixabay.com/photos/buildings-cn-tower-canada-colorful-2297210 - James Wheeler
skylineImage = Image.open('ex5/skyline.jpg')

# Crop the skyline image to just include the CN tower and save it as croppedSkyline.jpg
# Values in the crop() function are LEFT, TOP, RIGHT, BOTTOM coordinates in pixels
# of the original image
croppedImage = skylineImage.crop((220, 0, 256, 143))
croppedImage.save('ex5/croppedSkyline.jpg')

# Resize the cropped skyline image to a size of 108px wide by 429px tall
# and save it as resizedAndCroppedSkyline.jpg
resizedImage = croppedImage.resize((108, 429))
resizedImage.save('ex5/resizedAndCroppedSkyline.jpg')

# Rotate the resized image 32 degrees
# the expand=True flag expands the size to hold entire rotated image
rotatedImage = resizedImage.rotate(32, expand=True).save('ex5/rotatedSkyline.jpg')
