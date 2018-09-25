from PIL import Image
import PIL.ImageOps
import os

for img in os.listdir('source/'):
	print('Processing %s' % img)
	if img[-3:] != 'PNG':
		continue
	image = Image.open('source/%s' % img)
	inverted_image = PIL.ImageOps.invert(image)
	inverted_image.save('result/neg-%s' % img)
