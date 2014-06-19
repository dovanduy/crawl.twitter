#!/usr/bin/python 

import nltk, random
from nltk.corpus import names

def preprocess(sentence):
    ''' preprocess the sentences. 
    input is a raw sentence. 
    output is a list of tokens. '''
    s = sentence.strip(); 
    return [w for w in sentence.strip().split()]

def feature_selection(item):
    ''' build feature list from given item. '''
    s = preprocess(item)
    fs = {}
    for f in s:
        try:
            fs[f] += 1;
        except:
            fs[f] = 1; 
    return fs

def random_label():
    ''' assign a random label '''
    split = random.uniform(0,1)
    if split < 0.3: 
        return 0 
    else:
        return 1

if __name__ == '__main__':
    f = open('sample1.txt')
    ss = [(s, random_label()) for s in f] 
    random.shuffle(ss)
    
    fs = [(feature_selection(s), l) for (s, l) in ss]
    train_set, test_set = fs[500:], fs[:500]

    cl = nltk.NaiveBayesClassifier.train(train_set)

    ac = nltk.classify.accuracy(cl, test_set)
    print ac
    #pp1 = preprocess(line)
    #pp2 = feature_selection(pp1)
        #print pp2
    
# names = [(name, 'male') for name in names.words('male.txt')] + \
# [(name, 'female') for name in names.words('female.txt')]
# random.shuffle(names)

# featuresets = [(gender_features(n), g) for (n, g) in names]
# train_set, test_set = featuresets[500:], featuresets[:500]

# classifier = nltk.NaiveBayesClassifier.train(train_set)

# r1 = classifier.classify(gender_features("Min"))
# r2 = classifier.classify(gender_features("Shumin"))

# print r1, r2

# accuracy = nltk.classify.accuracy(classifier, test_set)
# print accuracy
# print classifier.labels()

##print classifier.show_most_informative_features(10)

