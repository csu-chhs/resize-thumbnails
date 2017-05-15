from PIL import Image
from resizeimage import resizeimage

IMAGE_SIZES = [36, 48, 72, 96, 144, 192, 180, 60, 120, 76, 152, 40, 80, 57, 114, 167, 29, 58, 50, 100]
IMAGE_FILE_NAME = 'fruit-square.png'
IMAGE_NAME = 'fruit-square'

for img_size in IMAGE_SIZES:
    fd_img = open(IMAGE_FILE_NAME, 'r')
    img = Image.open(fd_img)
    img = resizeimage.resize_thumbnail(img, [img_size, img_size])
    img.save(IMAGE_NAME + str(img_size) + '-.png', img.format)
    fd_img.close()
    print('Resized ' + str(img_size))
