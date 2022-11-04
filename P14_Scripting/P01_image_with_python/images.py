from PIL import Image,ImageFilter

img = Image.open('./Pokedex/4.1 pikachu.jpg')

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))


filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('./Pokedox_modified/4.1 Pikachu_blur.png','png')

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('./Pokedox_modified/4.1 Pikachu_sharp.png','png')

# filtered_img.show()    # this opens the image in the default image viewer

filtered_img = img.convert('L')#convert to gray
filtered_img.save('./Pokedox_modified/4.1 Pikachu_gray.png','png')

rotated_img = img.rotate(180)
rotated_img.save('./Pokedox_modified/4.1 Pikachu_rotate.png','png')


resized_img = img.resize((200,200)) #it is tuple   # but this will change the aspect ratio 
resized_img.save('./Pokedox_modified/4.1 Pikachu_resized.png','png')


box = (100,100,400,400)
cropped_img = img.crop(box)
cropped_img.save('./Pokedox_modified/4.1 Pikachu_croped.png','png')

img1 = Image.open('./Pokedex/6.1 astro.jpg')
img1.thumbnail((200,200))
img1.save('./Pokedox_modified/6.1 astro_thumbnail.png','png')