from PIL import Image
import numpy as np
import os
from svd_img import SVD_Image
from pathlib import Path

def get_image_data(name, path="", gray = False):
    if os.path.isfile(path+name):
        img = Image.open(path+name)
        if gray:
            image = np.array(img)
            gray_image = np.mean(image, axis=2)
            return gray_image
        else:
            img = Image.open(path+name)
            img_r, img_g, img_b = img.split()
            return np.asarray(img_r), np.asarray(img_g), np.asarray(img_b)
    raise FileNotFoundError("No such file")


def compress_img(file_path, percent_of_compression):
    # getting the color channels of an image in the form of matrices
    img_r, img_g, img_b = get_image_data(file_path)

    img = SVD_Image(img_r, img_g, img_b)
    img.leave_single_vals(percent_of_compression)

    # creation of new img
    img_matr = img.matrix
    img_denoised = Image.fromarray(img_matr)

    #save the img
    file_name = Path(file_path).name
    file_name = file_name[:-(file_name[::-1].find(".")+1)]
    img_denoised.save(f'static/compress_images/{file_name}_{percent_of_compression}.jpg')
