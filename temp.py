#libraries
import cv2
import cuantizador as ct
import numpy as np
from matplotlib import pyplot as plt
from sklearn.mixture import GaussianMixture as GMM


path = 'C:/Users/Daniel/Google Drive/imagenes_camaratrampa/Malpelo/DCIM/Segunda descarga/DCIM/100EK113/09200077.JPG'
img = cv2.imread(path)
img2 = img.reshape((-1,3))





