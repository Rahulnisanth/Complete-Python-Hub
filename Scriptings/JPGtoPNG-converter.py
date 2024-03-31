import os
import sys
from PIL import Image

# grab the first & second argument :
image_folder = sys.argv[0]
output_folder = sys.argv[1]

# check for new/ file existence :
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the image.jpg and save them in a new/ folder as png images :
for files in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{files}')
    clean_name = os.path.splitext(files)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('Done!')





