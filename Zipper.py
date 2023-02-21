# Script to zip the Training and Testing Images to load onto Google Colab
import shutil

shutil.make_archive('Image_set', 'zip', 'C:/Users/sgang/Desktop/BioTrillion_Challenge/Image_set')
print("Training and Testing Images Zipped")


