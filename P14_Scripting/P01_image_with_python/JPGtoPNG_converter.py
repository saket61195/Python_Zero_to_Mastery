
import sys
import os
from PIL import Image
input_folder = sys.argv[1]
ouput_folder = sys.argv[2]

if not os.path.exists(ouput_folder):
   os.makedirs(ouput_folder)

for filename in os.listdir(input_folder):
    img = Image.open(f'{input_folder}{filename}')
    clean_name = os.path.splitext(filename)[0] 
    img.save(f'{ouput_folder}/{clean_name}.png','png')
    print('all done')
 



#how to run
#python3 JPGtoPNG_converter.py Pokedex/ New/