from PIL import Image
import os
filepath="D:\parupadis\GIT-HUB\Image-Compressor2\image.png"

picture=Image.open(filepath)

picture.save("Compressed","JPEG", optimize=True, quality=10)