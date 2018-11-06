from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import csv
import  pickle
spamReader = csv.reader(open('train.csv', newline=''), delimiter='\t', quotechar='|')
train=[]
count=0
for row in spamReader:
	#print((row[2],row[3]))
	train.append((row[0],row[1]))
spamReader2 = csv.reader(open('test.csv', newline=''), delimiter='\t', quotechar='|')
newdata=[]
for row in spamReader2:
	#print(row)
	#print((row[2],row[3]))
	newdata.append((row[0],row[1]))
cl=None
mydict={'0':'negative','1': 'positive'}
try:
	pickle_in = open("trained.pickle","rb")
	cl=pickle.load(pickle_in)
except:
	print("in error")
	cl = NaiveBayesClassifier(train)
	file = open('trained.pickle','wb')
	pickle.dump(cl,file)

print(mydict[cl.classify("I feel amazing!")])
blob = TextBlob("The beer is good. But the hangover is horrible.", classifier=cl)
for s in blob.sentences:
     print(s)
     print(mydict[s.classify()])
print(mydict[cl.classify("I feel amazing!")])
print(cl.accuracy(newdata))
print(cl.show_informative_features(5))
