import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow
import random
import json
import pickle
import warnings 
warnings.filterwarnings("ignore")
userid="123"
with open("intents.json") as file:
	data = json.load(file)

# try:
# 	with open("data.pickle", "rb") as f:
# 	 	words, labels, training, output = pickle.load(f)
#except:
words = []
labels= []
docs_x= []
docs_y= []

for intent in data["intents"]:  #Loop on All question types
	for pattern in intent["patterns"]: #All patterns in a single question type,i.e; all the sentences
		wrds = nltk.word_tokenize(pattern) # divides based on space
		words.extend(wrds)
		docs_x.append(wrds) #docs_x contains all sentences as a list of words,i.e;list of lists of words
		docs_y.append(intent["tag"])

	if intent["tag"] not in labels:
		labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"] #stemmer reduces similar words into a single word
words = sorted(list(set(words))) #set makes sure it doesn't have duplicates

labels = sorted(labels)

training = []
output   = []

out_empty = [0 for _ in range(len(labels))]

for x,doc in enumerate(docs_x):
	bag = []

	wrds = [stemmer.stem(w) for w in doc]

	for w in words:
		if w in wrds:
			bag.append(1)
		else:
			bag.append(0)

	output_row = out_empty[:]
	output_row[labels.index(docs_y[x])] = 1

	training.append(bag)
	output.append(output_row)


training = np.array((training))
output = np.array((output))

with open("data.pickle", "wb") as f:
	pickle.dump((words, labels, training, output), f) # = pickle.load(f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None,len(training[0])])
net = tflearn.fully_connected(net, 100)
net = tflearn.fully_connected(net, 100)
net = tflearn.fully_connected(net, len(output[0]), activation = "softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

# try:
# 	model.load("model.tflearn")
# except:
model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")
