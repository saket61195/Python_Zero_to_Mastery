# question
# step 1 
# grab first and second argument
# step 2
# check is new/Exists if not create
# step 3
# loop through pokedox,
# covert images to png
# save to the new folder

import sys
import os
from PIL import Image
input_folder = sys.argv[1]
ouput_folder = sys.argv[2]
# print(input_folder,ouput_folder)

if not os.path.exists(ouput_folder):
   os.makedirs(ouput_folder)

for filename in os.listdir(input_folder):
    img = Image.open(f'{input_folder}{filename}')
    # clean_name = os.path.splitext(filename)
    clean_name = os.path.splitext(filename)[0] #it will remove the .(dot extension)
    # print(clean_name)
    # img.save(f'{ouput_folder}{clean_name}.png','png')
    #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
    img.save(f'{ouput_folder}/{clean_name}.png','png')
    print('all done')
 



#how to run
#python3 JPGtoPNG_converter.py Pokedex/ New/
#or complete path
#python3 JPGtoPNG_converter.py /home/saket/learning/python_programming/myowncode/P14_scripting/P01_image_with_python/Pokedex/ /home/saket/learning/python_programming/myowncode/P14_scripting/P01_image_with_python/New_folder/