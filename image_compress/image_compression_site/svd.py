import numpy as np
import os
from pathlib import Path

class SVD:
    "A simple class for workimg with svd"

    def __init__(self, matrix: np.ndarray) -> None:
        self._matrix = matrix
        self._u, self._e, self._vt = np.linalg.svd(matrix, full_matrices=False)
        self.r = len(self._e)
        self.rk = np.linalg.matrix_rank(matrix)
        self.ker = len(matrix) - self.rk
        
    def kernel(self)->np.ndarray:
        return self._vt[-self.ker:]

    def image(self)->np.ndarray:
        return self._u[:self.rk]

    def leave_singl_vals(self, k: int)->None:
        del_val = self._e[int((len(self._e)-1)*k/100)]
        self._e[self._e < del_val] = 0
        self.r = int((len(self._e)-1)*k/100)

    def __call__(self):
        return np.dot(self._u * self._e, self._vt)
    
    @property
    def VT(self):
        return self._vt
    
    @property
    def U(self):
        return self._u
    
    @property
    def E(self):
        return self._e
    
    @property
    def psevdo_A(self):
        psevdo_e = np.array([1/x if x!=0 else 0 for x in self._e])
        return np.round(np.dot(np.transpose(self._vt) * psevdo_e, np.transpose(self._u)), decimals=3)

class SVD_Image:
    """A simple class for compress image with svd"""

    matrix_to_save = [
        ["_u_r", "_e_r", "_vt_r"],
        ["_u_b", "_e_b", "_vt_b"],
        ["_u_g", "_e_g", "_vt_g"]
    ]

    def __init__(self, A_r=None, A_g=None, A_b=None) -> None:
        self._A_r = A_r
        self._A_g = A_g
        self._A_b = A_b
        print("start decompose")
        self._u_r, self._e_r, self._vt_r = np.linalg.svd(A_r, full_matrices=False)
        self._u_g, self._e_g, self._vt_g = np.linalg.svd(A_g, full_matrices=False)
        self._u_b, self._e_b, self._vt_b = np.linalg.svd(A_b, full_matrices=False)
        self.original_size = self._u_r.shape[0]*self._vt_r.shape[1]*3
        self.new_size = self.original_size
        print(self._u_r.shape, self._e_r.shape, self._vt_r.shape)
        self.r = len(self._e_r)
        print("finish decompose")
        
    def leave_single_vals(self, k: int)->None:
        del_val_r = self._e_r[int((len(self._e_r)-1)*k/100)]
        del_val_g = self._e_g[int((len(self._e_g)-1)*k/100)]
        del_val_b = self._e_b[int((len(self._e_b)-1)*k/100)]
        self._e_r[self._e_r < del_val_r] = 0
        self._e_g[self._e_g < del_val_g] = 0
        self._e_b[self._e_b < del_val_b] = 0
        
        r = int((len(self._e_r)-1)*k/100)

        self._e_r = self._e_r[:r]
        self._e_g = self._e_g[:r]
        self._e_b = self._e_b[:r]

        self._u_r = self._u_r[:, :r]
        self._vt_r = self._vt_r[:r, :]

        self._u_g = self._u_g[:, :r]
        self._vt_g = self._vt_g[:r, :]

        self._u_b = self._u_b[:, :r]
        self._vt_b = self._vt_b[:r, :]
        print(self._u_r.shape, self._e_r.shape, self._vt_r.shape)

    def recompose(self)->None:
        self._u_r, self._e_r, self._vt_r = np.linalg.svd(self._A_r, full_matrices=False)
        self._u_g, self._e_g, self._vt_g = np.linalg.svd(self._A_g, full_matrices=False)
        self._u_b, self._e_b, self._vt_b = np.linalg.svd(self._A_b, full_matrices=False)
    
    def save_decompose(self, path="./compress_image_files/", number=1):
        path_folder = path+str(number)+"/"
        if not os.path.exists(path_folder):
            os.makedirs(path_folder)
        
        for color in self.matrix_to_save:
            for el in color:
                file_path = os.path.join(path_folder, el)
                np.save(f'{file_path}.npy', getattr(self, el))

    def load_decompose(self, path="./compress_image_files/", number=1):
        path_folder = path+str(number)+"/"
        files_and_folders = os.listdir(path_folder)

        if not os.path.exists(path_folder):
            os.makedirs(path_folder)

        for item in files_and_folders:
            item_path = os.path.join(path_folder, item)
            if os.path.isfile(item_path):
                setattr(self, item[:-4], np.load(item_path))
            elif os.path.isdir(item_path):
                print(f"Это папка: {item}")
    
    @property
    def matrix(self):
        return np.dstack((np.array(np.dot(self._u_r * self._e_r, self._vt_r), dtype=np.uint8),
                          np.array(np.dot(self._u_g * self._e_g, self._vt_g), dtype=np.uint8),
                          np.array(np.dot(self._u_b * self._e_b, self._vt_b), dtype=np.uint8)))
