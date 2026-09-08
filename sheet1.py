import numpy as np
from matplotlib import pyplot as plt
t=np.empty((91,91,3))
t=np.array(t,dtype=np.int16) #le tableau est ici noir
t[:]=255 #le tableau devient blanc
t[:]=0 #A nouveau noir pour faire du vert dans la ligne suivante
t[:,:,1]=255 #le tableau devient vert

#print((t[0,0],t[90,90])) # On affiche les valeurs du premier pixel et du dernier pixel
t[:]=0 #A nouveau noir

for i in range(10):
    t[:,i*10,2]=255
    t[i*10,:,2]=255 #Quadrillage de bleu

plt.imshow(t)
plt.show()