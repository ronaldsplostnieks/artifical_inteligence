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
    # print(image)
    # print(np.array(image))
    # bildes.append(np.array(image))

