import os
import numpy as np
from PIL import Image

def split_file_name(file_path):
    file_name = os.path.basename(file_path)
    file_name_without_extension, file_extension = os.path.splitext(file_name)
    return file_name_without_extension, file_extension


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
