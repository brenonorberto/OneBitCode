from PIL import Image, ImageEnhance, ImageFilter

# 1 - Importando a imagem / convertendo em escala de cinza
img = Image.open('data/Kong.jpg')
# print(img)
img.show()

gray_img = img.convert('L')
# gray_img.show()

# 2 - Utilizando operações em imagem I
rotated_img = img.rotate(180)
# rotated_img.show()

transpose_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# transpose_img.show()

resize_img_small = img.resize((300, 200))
# resize_img_small.show()

resize_img_big = img.resize((1500, 1000))
# resize_img_big.show()

dim = (100, 100, 400, 400)
crop_img = img.crop(dim)
# crop_img.show()

# 3 - Utilizando operações em imagem II
enhance = ImageEnhance.Brightness(img)
bright_img = enhance.enhance(5)
# bright_img.show()

enhance = ImageEnhance.Contrast(img)
contrast_img = enhance.enhance(5)
# contrast_img.show()

# 4 - Utilizando filtros
filter_blur = img.filter(ImageFilter.BLUR)
# filter_blur.show()

filter_contour = img.filter(ImageFilter.CONTOUR)
filter_contour.show()

