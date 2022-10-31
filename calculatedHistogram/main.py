import cv2
import numpy as np
from matplotlib import pyplot as plt

myImage = cv2.imread("image.jpg", 0)
cv2.imshow("..Image Processing..", myImage)
cv2.waitKey()

shape = myImage.shape
height = shape[0]
width = shape[1]

arrayOfHist = np.zeros(256)

for i in range(0, height):
    for j in range(0, width):
        arrayOfHist[myImage[i][j]] = arrayOfHist[myImage[i][j]] + 1

print(arrayOfHist)

plt.figure("Histogram")
plt.xlabel("0-255 Color Values of Pixels")
plt.ylabel("Intensitive of the Points")
plt.plot(arrayOfHist)
plt.show()
