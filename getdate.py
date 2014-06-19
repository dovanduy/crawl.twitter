#!/usr/bin/env python

import tweetstream, twitter

stream = tweetstream.SampleStream("gsmsteve@gmail.com", "825123")

api = twitter.Api(consumer_key='NINW6eFEgEAOUAFAX5bVpQ', 
                  consumer_secret='SjJDB2Bpk0IjiEWlptCUkJsluq17tockkAQqJCSs', 
                  access_token_key='SjJDB2Bpk0IjiEWlptCUkJsluq17tockkAQqJCSs', 
                  access_token_secret='QxwE8socZx7gxcNJlrKMveDYWeyhIir3cvh2KgO5wHI')

print api.VerifyCredentials()
# statuses = api.GetUserTimeline('gsm1011')

# print [s.user.name for s in statuses] 

users = api.GetFriends()
print [u.name for u in users] 
