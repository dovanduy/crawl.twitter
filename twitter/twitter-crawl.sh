#!/usr/bin/env bash

# Crawling twitter data 350 times every hour. 

cnt=0; 
javac -cp ./lib/twitter4j-core-4.0.1.jar:. GetTweets.java

while true; do 
    # echo $cnt 
    java -cp ./lib/twitter4j-core-4.0.1.jar:. GetTweets >> tweets.txt 
    cnt=$(($cnt + 1))
    sleep 5
done
