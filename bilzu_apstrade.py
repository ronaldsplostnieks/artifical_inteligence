from PIL import Image
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.ensemble import RandomForestClassifier


bildes = []
label = []

bilzu_adrese = 'bildes/'


for nosaukums in os.listdir(bilzu_adrese):
    image = Image.open(os.path.join(bilzu_adrese,nosaukums))
    bildes.append(np.array(image))
    if "maja" in nosaukums:
        label.append(1)
    else:
        label.append(0)

