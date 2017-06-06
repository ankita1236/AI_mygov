from nltk.corpus import words
aawords = words.words()
with open('removedhindi.txt','r') as f:

	for line in f.readlines():
	
		
	        for w in line.split():
         		if w in aawords:
				print w
				output = open("output.txt", "a")
				output.write(w)
				output.write(" ")
		
