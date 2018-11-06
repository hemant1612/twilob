from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import csv
spamReader = csv.reader(open('train.csv', newline=''), delimiter='\t', quotechar='|')
train=[]
count=0
for row in spamReader:
	count+=1
	if count==20000:
		break
	#print((row[2],row[3]))
	train.append((row[2],row[3]))
mydict={'0':'negative','1': 'somewhat negative','2': 'neutral','3': 'somewhat positive','4' :'positive'}
cl = NaiveBayesClassifier(train)








print(mydict[cl.classify("I feel amazing!")])
blob = TextBlob("The beer is good. But the hangover is horrible.", classifier=cl)
for s in blob.sentences:
     print(s)
     print(mydict[s.classify()])
print(mydict[cl.classify("I am nervous")])
print(mydict[cl.classify("I hate him")])
print(mydict[cl.classify("that was a boring and slow movie")])
cl.show_informative_features(5)

spamReader2 = csv.reader(open('testing.csv', newline=''), delimiter='\t', quotechar='|')
tra = []
for row in spamReader2:
    count+=1
    tra.append((row[2],row[3]))

print(cl.accuracy(tra))