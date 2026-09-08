import numpy as np
from matplotlib import pyplot as plt
image=plt.imread("data/les-mines.jpg")
image.flags.writeable
#plt.imshow(image)

type(image) # type de l'image : <class 'numpy.ndarray'>
np.shape(image) # Forme de l'image :  (533, 800, 3)
type(image[0,0,0]) # Nombre d'octets des entiers encodés et type des entiers: <class 'numpy.uint8'>
print(image.max(),image.min()) #max et min
imbis=image[:10,:10]
#plt.imshow(imbis)

imsliced=image[:,::10]
#plt.imshow(imsliced)
(l, c) = (100, 200)

immid=image[533//2-l//2:533//2+l//2,400-c//2:400+c//2]
#plt.imshow(immid)
imred,imgreen,imblue = image[:,:,0], image[:,:,1] , image[:,:,2]
"""plt.imshow(imred)
plt.show()
plt.imshow(imgreen)
plt.show()
plt.imshow(imblue)
plt.show() #Séparation des canaux
#Corrigeons ces images d'apparences vertes ->

imred2 = np.copy(image)
imred2[:,:,1]=0
imred2[:,:,2]=0
plt.imshow(imred2)
plt.show()

imgreen2 = np.copy(image)
imgreen2[:,:,0]=0
imgreen2[:,:,2]=0
plt.imshow(imgreen2)
plt.show()

imblue2 = np.copy(image)
imblue2[:,:,1]=0
imblue2[:,:,0]=0
plt.imshow(imblue2)
plt.show()
#Séparation des canaux en gardant leur couleur

im5 = np.copy(image)
#on remplace un carré 200*200 par un carré de couleur (219, 112, 147)
im5[333:,600:]=(219, 112, 147)
plt.imshow(im5)
plt.show()
#on remplace un carré 200*200 par un carré blanc rayé de rouge
im6= np.copy(image)
im6[333:,600:]=(255, 255, 255)
im6[333::3,600:]=(255,0,0)
im6[333:,600::3]=(255,0,0)
plt.imshow(im6)
plt.show()

# --- instauration d'un canal alpha ---

im7 = np.empty((533,800,4),dtype=image.dtype)
im7[:,:,:3]= image
im7[:,:,3] =128
plt.imshow(im7)
plt.show()

# --- image en niveaux de gris en float ---
"""
im8=np.empty((533,800,3))
im8[:,:,:]=(image[:,:,:]/255)
plt.imshow(im8)
plt.show()

im9=im8.mean(2) #image en niveaux de gris
plt.imshow(im9)
plt.show()

im10=np.copy(im8) #image en niveaux de gris avec la correction
im10= 0.299 * im8[:,:,0] + 0.587 * im8[:,:,1] + 0.114 * im8[:,:,2]
plt.imshow(im10)
plt.show()