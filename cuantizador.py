import cv2
import numpy as np

def cuantizador(image):
    maximum = image.max()
    image = image / maximum
    fil, col = image.shape
    for i in range( fil ):
        for j in range( col ):
            value = image[i,j]

            if (value > 0.9):
                value = 1
            elif(value > 0.8):
                value = 0.9
            elif (value > 0.7):
                value = 0.8
            elif (value > 0.6):
                value = 0.7
            elif (value > 0.5):
                value = 0.6
            elif (value > 0.4):
                value = 0.5
            elif (value > 0.3):
                value = 0.4
            elif (value > 0.2):
                value = 0.3
            elif (value > 0.1):
                value = 0.2
            else:
                value = 0

            image[i,j] = value
    
    image = maximum * image
    print(image)
    return image

def maxPool(image):
    fil, col = image.shape
    print(str(image.shape))
    image2 = np.ones(image.shape)
    PlusX = 100
    PlusY = 100
    PlusY1 = PlusY + 1
    PlusX1 = PlusX + 1
    array =  np.ones( (PlusY,PlusX))
    sample =  np.ones( (PlusY,PlusX))
    for i in range (fil-PlusY):
        for j in range (col-PlusY):
            sample = image[i : i + PlusY, j: j + PlusX]
            
            Max = sample.mean()
            
            image2[i : i + PlusY, j: j + PlusX] = Max * array
            j = j + PlusX
        i = i + PlusY
    return image2