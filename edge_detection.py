from PIL import Image
from PIL import ImageFilter

img = Image.open("Bilder_BSP/filter1.jpg")
#img.show()

im = img.filter(ImageFilter.EDGE_ENHANCE)
im.show()
