from PIL import Image
import numpy as np
import os
from svd import SVD_Image
from pathlib import Path

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

def save_img(path):
    img = SVD_Image()
    img.load_decompose()

    img_matr = img.matrix
    img_denoised = Image.fromarray(img_matr)
    img_denoised.save(path)


def compress_img(file_path, percent_of_compression):
    img_r, img_g, img_b = get_image_data(file_path)
    img = SVD_Image(img_r, img_g, img_b)
    img.leave_single_vals(percent_of_compression)

    img_matr = img.matrix
    img_denoised = Image.fromarray(img_matr)
    file_name = Path(file_path).name
    file_name = file_name[:-(file_name[::-1].find(".")+1)]
    img_denoised.save(f'static/compress_images/{file_name}_{percent_of_compression}.jpg')
    

if __name__ == "__main__":
    # compress_img("static/upload_images/CloneWars.jpg", 99)
    import os

    file_path = "/home/python/projects/course_work/image_compress/app/static/upload_images/e374ef71a7eb88cffa8c91fbaacfeedf.jpeg"  # Укажите путь к вашему файлу

    # Используйте os.path.basename() для получения имени файла
    file_name = os.path.basename(file_path)

    # Используйте os.path.splitext() для разделения имени файла и расширения
    file_name_without_extension, file_extension = os.path.splitext(file_name)

    print("Имя файла без расширения:", file_name_without_extension)
    print(file_extension)
