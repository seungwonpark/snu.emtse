from PIL import Image
import PIL.ImageOps
import os

for img in os.listdir('source/'):
	if img[-3:].lower() != 'png':
		continue
	print('Processing %s' % img)
	image = Image.open('source/%s' % img)
	inverted_image = PIL.ImageOps.invert(image)
	inverted_image.save('result/neg-%s' % img)
