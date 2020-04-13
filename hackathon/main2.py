import warnings 
warnings.filterwarnings("ignore")
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy as np
import tflearn
import tensorflow
import random
import json
import pickle


userid = "123"

with open("intents.json") as file:
	data = json.load(file)

try:
	with open("data.pickle", "rb") as f:
	 	words, labels, training, output = pickle.load(f)
	 	#print(labels)
except:
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

	#labels = sorted(labels)

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
#net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation = "softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
	model.load("model.tflearn")
except:
	model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
	model.save("model.tflearn")


def bag_of_words(s, words):
	bag = [0 for _ in range(len(words))]
	#print(len(words))
	s_words = nltk.word_tokenize(s)
	s_words = [stemmer.stem(word.lower()) for word in s_words]

	small_len = np.array([len(s) for s in s_words])
	small_words = (small_len > 3).astype(int)
	small_words = small_words
	sums = np.sum(small_words)

	for se in s_words:
		for i,w in enumerate(words):
			if w == se:
				bag[i] = 1

	return np.array((bag)),sums

asked_q = []
context = {}
resp = ["Mate,you have asked it recently,please ask any other","Please change your query, you have asked it just before","You have made a similar statement before,please change it"]

def chat(msg):
	#print("Start talking with the bot (type quit to stop)!")
	#flag = True
	while True:
		inp = msg
		low = stemmer.stem(inp.lower())
		if low == "":
			return "Please ask something,I am here to chat with you :)"
		if low == "quit" or low == "bye" or low == "good bye" or low == "goodbye":
			return ""

		bagof,sums = bag_of_words(inp, words)
		results = model.predict([bagof])[0]
		#print(results)

		results2 = np.array(results)
		results1 = (results2 >= 0.25).astype(int)
		results3 = list(results1)
		#results1 = int(results1)
		#print(results1)
		valid =[]
		
		for y,r in enumerate(results1):
			if(r == 1):
				#print(y)
				#print(results2[y])
				#print(int(labels[y][3:]))
				#print(sums)
				if(sums != 0 or int(labels[y][3:]) < 28):
					valid.append(labels[y])
				#print(labels[y])
		#print(valid)
		ab = 0
		if results3 in asked_q:
			valid = []
			ab = 1
			return random.choice(resp)
		elif 1 in results3:
			asked_q.append(results3)

		if(len(asked_q) > 5):
			asked_q.pop(0)

		abc = 0
		for i1 in data["intents"]:
			if i1["tag"] in valid:
				#print("good0")
				if "context_set" in i1:
					context[userid] = i1["context_set"]

				if not "context_filter" in i1 or (userid in context and "context_filter" in i1 and i1["context_filter"] == context[userid]):
					#print("good1")
					return random.choice(i1["responses"])  
					abc = 1
		notget = ["I didn't get you, Can you rephrase your statement or ask another","Oops!! looks like you got me in trouble understanding you ,can you ask again :)"]

		if((not valid) and (ab == 0)):
			return random.choice(notget)
			abc = 2
		if((abc == 0) and (ab == 0)):
			return random.choice(notget)
