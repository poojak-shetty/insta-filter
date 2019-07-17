#import Image from PIL
from PIL import Image
#Load Images into objects
base_img=Image.open("base.jpeg")
img_filter=Image.open("download.jpg")
#set 0/p image size
size=(760,760)
#resize all images to o/p size
base_img=base_img.resize(size)
img_filter=img_filter.resize(size)
r,g,b=base_img.split()
R,G,B=img_filter.split()
im=Image.merge("RGB",(R,g,B))
im=Image.merge("RGB",(r,Gg,b))
#im.save('1_merged.jpg')
