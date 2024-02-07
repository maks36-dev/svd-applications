import numpy as np

class SVD_Image:
    """A simple class for compress image with svd"""

    def __init__(self, A_r=None, A_g=None, A_b=None) -> None:
        # save input matrix
        self._A_r = A_r
        self._A_g = A_g
        self._A_b = A_b

        # svd
        self._u_r, self._e_r, self._vt_r = np.linalg.svd(A_r, full_matrices=False)
        self._u_g, self._e_g, self._vt_g = np.linalg.svd(A_g, full_matrices=False)
        self._u_b, self._e_b, self._vt_b = np.linalg.svd(A_b, full_matrices=False)

        
    def leave_single_vals(self, k: int)->None:
        """A function that leaves k percent singular values"""

        # calculate position of the last value
        r = int((len(self._e_r)-1)*k/100)
        del_val_r = self._e_r[r]
        del_val_g = self._e_g[r]
        del_val_b = self._e_b[r]

        # delete values after last
        self._e_r[self._e_r < del_val_r] = 0
        self._e_g[self._e_g < del_val_g] = 0
        self._e_b[self._e_b < del_val_b] = 0

        # remake svd of img
        self._e_r = self._e_r[:r]
        self._e_g = self._e_g[:r]
        self._e_b = self._e_b[:r]

        self._u_r = self._u_r[:, :r]
        self._vt_r = self._vt_r[:r, :]

        self._u_g = self._u_g[:, :r]
        self._vt_g = self._vt_g[:r, :]

        self._u_b = self._u_b[:, :r]
        self._vt_b = self._vt_b[:r, :]

    def recompose(self)->None:
        """Initial values of the color channels"""

        self._u_r, self._e_r, self._vt_r = np.linalg.svd(self._A_r, full_matrices=False)
        self._u_g, self._e_g, self._vt_g = np.linalg.svd(self._A_g, full_matrices=False)
        self._u_b, self._e_b, self._vt_b = np.linalg.svd(self._A_b, full_matrices=False)
    
    @property
    def matrix(self):
        """Retrun the whole matrix"""
        
        return np.dstack((np.array(np.dot(self._u_r * self._e_r, self._vt_r), dtype=np.uint8),
                          np.array(np.dot(self._u_g * self._e_g, self._vt_g), dtype=np.uint8),
                          np.array(np.dot(self._u_b * self._e_b, self._vt_b), dtype=np.uint8)))
