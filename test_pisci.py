import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import Model
from sklearn.preprocessing import LabelBinarizer
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob


rekonstruisan_model = keras.models.load_model("model_pisci.h5")

df1 = pd.read_csv("test.csv")
df1.rename(columns={ '0':'tekst', '1':'pisac'}, 
                 inplace=True)

#funkcija sample sluzi za nasumicno mesanje samplova  
df1 = df1.sample(frac=1)
df1.size



# sece na maksimalno 500 karaktera po sample-u
max_len = 500 
# razmatra prvih 10 000 reci
max_words = 10000 

lista = df1['tekst'].to_list()

# import tokenizer, gleda se samo prvih 10 000 reci
tokenizer = Tokenizer(num_words=max_words) 
# fitujemo tokenizer na listu tekstova
tokenizer.fit_on_texts(lista) 
# konvertujemo tekst u sekvence
sekvence = tokenizer.texts_to_sequences(lista) 

word_index = tokenizer.word_index
print('Found %s unique tokens. ' % len(word_index))

 # pravimo array sekvenci sa maksimalnom duzinom 500 
data = pad_sequences(sekvence, maxlen=max_len)
print('Data Shape: {}'.format(data.shape))


pisac_enkoder = OneHotEncoder()
#ubacujemo data u promenjivu X
X = np.array(data)

#binarizujemo pisce, koji su kategoricki nominalni tip
y = pd.get_dummies(df1['pisac'])
#uzimamo nazive kolona kako bismo posle mogli da vratimo prezimena pisaca
kolone = list(y.columns.values)
#print(kolone)

y = y.to_numpy()


early_stop = keras.callbacks.EarlyStopping(monitor='acc', patience=3)
history = rekonstruisan_model.fit(X_train, y_train, epochs=50, batch_size=128, 
                    callbacks=[early_stop])