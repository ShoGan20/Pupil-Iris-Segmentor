import numpy as np
import cv2
from PIL import Image, ImageDraw
import pandas as pd
import os
import glob

dir = os.path.dirname(__file__)
#file_dir = os.path.join(dir, 'training_set/groundtruth/') # Setting path for Training Images
file_dir = os.path.join(dir, 'testing_set/groundtruth/') # Setting path for Testing Images
print(file_dir)
csv_files = glob.glob(file_dir + '*.csv')

for csv_file in csv_files:
    data = pd.read_csv(csv_file)
    base_name = os.path.basename(csv_file)
    output_name = base_name[:-4]+".png"
    #output_dir = os.path.join(dir, 'training_set/masks/'+output_name).replace("\\", "/") # Setting path for Training Images
    output_dir = os.path.join(dir, 'testing_set/masks/' +output_name).replace("\\", "/") # Setting path for Testing Images

    # Iris Values
    iris_x_coord = data['coord_i_true_x'][0]
    iris_y_coord = data['coord_i_true_y'][0]
    iris_x_rad = data['radiusX_i_true'][0]
    iris_y_rad = data['radiusY_i_true'][0]
    iris_angle = data['theta_i_true'][0]

    # Pupil Values
    pupil_x_coord = data['coord_p_true_x'][0]
    pupil_y_coord = data['coord_p_true_y'][0]
    pupil_x_rad = data['radiusX_p_true'][0]
    pupil_y_rad = data['radiusY_p_true'][0]
    pupil_angle = data['theta_p_true'][0]

    # Defining BB for Iris
    iris_left_corner = (iris_x_coord - iris_x_rad, iris_y_coord - iris_y_rad)
    iris_right_corner = (iris_x_coord + iris_x_rad, iris_y_coord + iris_y_rad)
    iris_boundaries = [iris_left_corner, iris_right_corner]

    # Defining BB for Pupil
    pupil_left_corner = (pupil_x_coord - pupil_x_rad, pupil_y_coord - pupil_y_rad)
    pupil_right_corner = (pupil_x_coord + pupil_x_rad, pupil_y_coord + pupil_y_rad)
    pupil_boundaries = [pupil_left_corner, pupil_right_corner]

    img = Image.open(output_dir)

    # creating circles around Iris and Pupil
    img.paste( (0,0,0), [0,0,img.size[0],img.size[1]]) # Black out the image first
    iris_draw = ImageDraw.Draw(img)
    iris_draw.ellipse(iris_boundaries, fill="#ffffff")  #Draw Iris Circle
    pupil_draw = ImageDraw.Draw(img)
    pupil_draw.ellipse(pupil_boundaries, fill="#ff0000") # Draw Pupil Circle
    
    # Saving the image
    img.save(output_dir)