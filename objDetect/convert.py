from PIL import Image
#Open image using Image module
img = "try.jpeg"
im = Image.open(img)
rgb_im = im.convert('RGB')
name = img.split('.')
name = name[0]+".png"
print(name)
rgb_im.save(name)