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

    def __call__(self)->np.ndarray:
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
    def psevdo_matrix(self):
        psevdo_e = np.array([1/x if x!=0 else 0 for x in self._e])
        return np.dot(np.transpose(self._vt) * psevdo_e, np.transpose(self._u))

