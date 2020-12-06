# To install PIL - pip3 install Pillow
from PIL import Image
import os


#################################################################################
# Path
#################################################################################


# Current directory of python file
cur_path = os.path.dirname(__file__)

# Directory where all images are stored
dir_images = cur_path + os.path.sep + "images" + os.path.sep


#################################################################################
# Colors
#################################################################################


doctrine_red = "#ff8080" #rgb(255, 128, 128)
doctrine_blue = "#80e0ff" #rgb(128, 224, 255)
doctrine_yellow = "#ffff80" #rgb(255, 255, 128)
doctrine_green = "#a9ffa9" #rgb(169, 255, 169)

ppt_blue = "#0070c0" #rgb(0, 112, 192)
ppt_red = "#ff0000" #rgb(255, 0, 0)
ppt_yellow = "#ffff00" #rgb(255,255,0)
ppt_green = "#00b050" #rgb(0, 176, 80)


#################################################################################
# Read/Write File
#################################################################################


def get_image_obj(file):
	return Image.open(file)

def copy_to_png_directory(file):
	image = Image.open(dir_images + file)
	image.save(dir_images + file)

def convert_to_png(file):
	image = Image.open(dir_images + file)
	fn, fext = os.path.splitext(file)
	image.save('{}{}.png'.format(dir_images, fn))

def convert_all_to_png():

	# Step through all images
	for file in os.listdir(dir_images):

		if file.endswith('.jpg'):
			convert_to_png(file)

		elif file.endswith('.png'):
			copy_to_png_directory(file)
			


#################################################################################
# Image Manipulation
#################################################################################


def resize(image, x, y):
	image.resize(x, y)

def replace_color(image, old_color, new_color):
	# TODO replace color in image


#################################################################################
# Build
#################################################################################


def main():
	return True

if __name__ == '__main__':
	main()
