from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import csv
spamReader = csv.reader(open('train_amazon.csv', newline=''), delimiter='\t', quotechar='|')
train=[]
count=0
for row in spamReader:
	count+=1
	if count==3000:
		break
	if(len(row) == 2):
	    train.append((row[0],row[1]))
	else:
	    print(row)
    

#	train.append((row[1],row[2]))
mydict={'1':'negative','2': 'somewhat negative','3': 'neutral','4': 'somewhat positive','5' :'positive'}
cl = NaiveBayesClassifier(train)

cl.show_informative_features(30)

print(mydict[cl.classify("I feel amazing!")])
print(mydict[cl.classify("poor quality")])



spamReader2 = csv.reader(open('testing_amazon.csv', newline=''), delimiter='\t', quotechar='|')
tra = []
for row in spamReader2:
    count+=1
    tra.append((row[0],row[1]))

print(cl.accuracy(tra))