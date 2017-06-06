import nltk
import csv
import sys
reload (sys)
sys.setdefaultencoding('utf8')
#f=open('n.txt','r')

with open('cleaned.txt','r') as f:

	for line in f.readlines():
		tokens = nltk.word_tokenize(line)
		tagged = nltk.pos_tag(tokens)
		nouns = [word for word,pos in tagged \
		if (pos == 'NN'  or pos == 'NNS' and pos!='FW')]
		downcased = [x.lower() for x in nouns]
		joined = " ".join(downcased).encode('utf-8')
		into_string = str(nouns)
	
		output = open("nounf.txt", "a")
		output.write(joined)
		output.write("\n")
output.close()
