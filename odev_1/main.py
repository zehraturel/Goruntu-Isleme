import matplotlib.pyplot as plt
import numpy as np
import cv2

fotoKonumu = 'balik.jpg'  
foto = cv2.imread(fotoKonumu)
griFoto = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

cv2.imshow('fotograf',griFoto)
cv2.waitKey(0)
satir, sutun = griFoto.shape

histogram = np.zeros(256, dtype=int)
for i in range(satir):
    for j in range(sutun):
        griSeviye = int(griFoto[i, j])
        histogram[griSeviye] += 1
        
plt.bar(np.arange(256), histogram, color='gray')
plt.title('Histogram')
plt.xlabel('Gri Seviye')
plt.ylabel('Frekans')
plt.show()
