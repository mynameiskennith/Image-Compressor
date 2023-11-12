from PIL import Image

filepath="D:\parupadis\GIT-HUB\Image-Compressor2\image.png"

picture=Image.open(filepath)

picture.save("10%","jpeg", optimize=True, quality=10)