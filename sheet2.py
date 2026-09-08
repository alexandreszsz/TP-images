import numpy as np
from matplotlib import pyplot as plt
image=plt.imread("data/les-mines.jpg")
image.flags.writeable
plt.imshow(image)
plt.show()
