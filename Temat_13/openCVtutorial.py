# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image = cv2.imread('image.png')
  
# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))

# pixel with 100, 100 for height and width.
(B, G, R) = image[100, 100]
  
# Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))
  
# We can also pass the channel to extract 
# the value for a specific channel
B = image[100, 100, 0]
print("B = {}".format(B))

# slicing the pixels of the image
roi = image[100 : 500, 200 : 700]
# resize() function takes 2 parameters, 
# the image and the dimensions
resize = cv2.resize(image, (800, 800))

# Calculating the ratio
ratio = 800 / w
  
# Creating a tuple containing width and height
dim = (800, int(h * ratio))
# Resizing the image
resize_aspect = cv2.resize(image, dim)

# Calculating the center of the image
center = (w // 2, h // 2)
# Generating a rotation matrix
matrix = cv2.getRotationMatrix2D(center, -45, 1.0) 
  
# Performing the affine transformation
rotated = cv2.warpAffine(image, matrix, (w, h))

# We are copying the original image, 
# as it is an in-place operation.
output = image.copy()
# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(output, (1500, 900), 
                          (600, 400), (255, 0, 0), 2)
# Copying the original image
output = image.copy()
  
# Adding the text using putText() function
text = cv2.putText(output, 'OpenCV Demo', (500, 550), 
                   cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)

