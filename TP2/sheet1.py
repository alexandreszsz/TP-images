import numpy as np
import matplotlib.pyplot as plt

# en mode notebook, ça peut être utile de choisir un mode interactif
# comme par exemple celui-ci
# par contre ça nécessite de faire un `pip install ipympl`
# %matplotlib ipympl
# pour jouer les sons qu'on va produire

from IPython.display import Audio,display
from scipy.io import wavfile
RATE = 44_100
LA = 440
DO = 523.25

"""1.Pour une durée de 1 seconde il faut 44100 échantillons fois 1 seconde.
2.L'équation mathématique de la position est : f(t) =$cos(2pi phi t)$"""

t=np.linspace(0,2*3.14,44100)
f=np.sin(2 *3.14 *440 *t)
display(Audio(f,44100))