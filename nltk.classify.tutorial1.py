#!/usr/bin/python 

import nltk, random
from nltk.corpus import names

def gender_features(word):
    return {'length':len(word),'last_letter':word[-1],'first_letter':word[0]}

names = [(name, 'male') for name in names.words('male.txt')] + \
[(name, 'female') for name in names.words('female.txt')]
random.shuffle(names)

featuresets = [(gender_features(n), g) for (n, g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]

classifier = nltk.NaiveBayesClassifier.train(train_set)

r1 = classifier.classify(gender_features("Min"))
r2 = classifier.classify(gender_features("Shumin"))

print r1, r2

accuracy = nltk.classify.accuracy(classifier, test_set)
print accuracy
print classifier.labels()

##print classifier.show_most_informative_features(10)

