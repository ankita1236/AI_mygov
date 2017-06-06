print "Creating the bag of words...\n"
from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup   
import numpy as np
import codecs
import pandas as pd
# Initialize the "CountVectorizer" object, which is scikit-learn's
# bag of words tool.  
with open ('nounf.txt','r') as f:
	train= f.readlines()
vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000) 

# fit_transform() does two functions: First, it fits the model
# and learns the vocabulary; second, it transforms our training data
# into feature vectors. The input to fit_transform should be a list of 
# strings.
train_data_features = vectorizer.fit_transform(train)

# Numpy arrays are easy to work with, so convert the result to an 
# array
train_data_features = train_data_features.toarray()
print train_data_features.shape
vocab = vectorizer.get_feature_names()
print vocab


# Sum up the counts of each vocabulary word
dist = np.sum(train_data_features, axis=0)

# For each, print the vocabulary word and the number of times it 
# appears in the training set
for tag, count in zip(vocab, dist):
    print count, tag
with codecs.open('t.txt','r',encoding='utf-8',errors='ignore') as f1:
	test=f1.readlines()

print "Training the random forest..."
from sklearn.ensemble import RandomForestClassifier

# Initialize a Random Forest classifier with 100 trees
forest = RandomForestClassifier(n_estimators = 100) 

# Fit the forest to the training set, using the bag of words as 
# features and the sentiment labels as the response variable
#
# This may take a few minutes to run
forest = forest.fit( train_data_features, train)



test_data_features = vectorizer.transform(test)
print test_data_features
test_data_features = test_data_features.toarray()

print test_data_features.shape
# Use the random forest to make sentiment label predictions
result = forest.predict(test_data_features)
print result








