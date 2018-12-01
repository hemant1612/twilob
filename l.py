from textblob import TextBlob
#from textblob.classifiers import NaiveBayesClassifier,DecisionTreeClassifier
#import csv
#spamReader = csv.reader(open('training_amazon_new.csv', newline=''), delimiter='\t', quotechar='|')
#train=[]
#count=0
#for row in spamReader:
##	count+=1
##	if count>200:
##	    break
#	if(len(row) == 2):
#            print(row[0])
#	    train.append(row[0],row[1])
#	else:
#	    print(row)
#    
#
##	train.append((row[1],row[2]))
#mydict={'1':'negative','2': 'somewhat negative','3': 'neutral','4': 'somewhat positive','5' :'positive'}
#cl = NaiveBayesClassifier(train)
#
##
##cl.show_informative_features(30)
#
#print(cl.classify("very bad camera"))
#print(mydict[cl.classify("poor product")])
#print(mydict[cl.classify("worst")])
#
#
#
#spamReader2 = csv.reader(open('testing_amazon.csv', newline=''), delimiter='\t', quotechar='|')
#tra = []
#for row in spamReader2:
#    tra.append((row[0], row[1]))
#
#print(cl.accuracy(tra))


#testimonial = TextBlob("battery is poor but display is excellent")
#print(testimonial.sentiment)
#
#print(testimonial.sentiment.polarity)
#

import nltk
conj = ['and' , 'nor','but','or','yet','so','yet','and','for','nor', 'or','but','so','for','or','nor','yet','but','and', 'so']

inputstring = ' battery is good but camera is poor'
for i in range(len(conj)):
    inputstring = inputstring.replace(conj[i],',')
    


from nltk.tokenize import sent_tokenize
all_sent = sent_tokenize(inputstring)
print(all_sent)







