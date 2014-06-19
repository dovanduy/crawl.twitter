#!/usr/bin/env python 

# Create tag cloud for twitter tweets. 

from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

from nltk.corpus import stopwords
import sys, random

text = ''

def make_tag_cloud(): 
    for line in sys.stdin:
        try: 
            text += ' ' + line.strip().lower()
        except:
            pass
    
    tags = make_tags(get_tag_counts(text), maxsize=150)
    create_tag_image(tags, sys.argv[1] + '.png', size=(1024, 768))

def tokenize(sentence):
    ''' tokenize given sentence '''
    words = []
    words = [w for w in sentence.strip().split()]
    return words

def remove_stop_words(word_list):
    return [w for w in word_list if not w in stopwords.words('english')]

def label_tweet(tweet):
    try:
        t = tweet.strip().split('\t')[2]
        if(len(t.split()) < 5): return

        print '>>>>: ', t
        label = raw_input('Your label is:')
        print '-->>: ', t, '\t', label
        print
    except:
        pass
    
def clean_tweet(tweet):
    # TODO. 
    pass

if __name__ == '__main__':
    if sys.argv[1] == "-s":
        for line in sys.stdin:
            line = line.strip()
            if line == "":
                continue 
            print remove_stop_words(tokenize(line))
    elif sys.argv[1] == "-l":
        if(sys.argv[2].strip() == ""): exit
        for line in open(sys.argv[2]):
            line = line.strip()
            if line == "": continue
            label_tweet(line)
