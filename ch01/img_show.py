import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('ch01/img/cactus.png')

plt.imshow(img)
plt.show()