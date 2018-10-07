from loadEquations import load_equations
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import *
from keras.models import Model
import numpy as np


(inputs,targets) = load_equations("./equations.txt")
tokenizer = Tokenizer()
tokenizer.fit_on_texts(inputs)
inputs = tokenizer.texts_to_sequences(inputs)
inputs = pad_sequences(inputs,value=0)
num_tokens = (list(tokenizer.word_index.values())[-1])
targets = np.array(targets)

print(inputs[0])

print(inputs.shape)
print(targets.shape)

input_layer = Input(shape=(inputs.shape[1],))
embed_layer = Embedding(num_tokens + 1,10,input_length=inputs.shape[1])(input_layer)
gru = Bidirectional(GRU(30))(embed_layer)

relu = Dense(100, activation='relu')(gru)
relu = Dense(100, activation='relu')(relu)

output = Dense(1,activation='linear')(relu)

model = Model(inputs=input_layer, outputs=output)
model.compile(optimizer='adam',
              loss='MSE')
print(model.summary())
model.fit(inputs,targets,epochs=100)


while True:
    text= input()
    text = tokenizer.texts_to_sequences([text])
    text = pad_sequences(text,maxlen=inputs.shape[1],value=0)
    print(model.predict(np.array(text)))

