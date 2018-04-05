# TODO: Dig into comments for a subreddit, etc., for parsing and interpreting.

import praw
import os
import json

cwd = os.getcwd()
with open(cwd + '/local/config.json', 'r') as f:
	config = json.load(f)

reddit = praw.Reddit(user_agent=config['user_agent'],
                     client_id=config['client_id'], 
					 client_secret=config['client_secret'])

keyword = 'freedom'
sub = 'socialism'
words = {}
omit = ['the', 'a', 'an', 'that', 'this', 'to', 'for', 'of', 'on', 'in', 'but', 'and', '-',
         'is', 'are', 'was', '[oc]']

subreddit = reddit.subreddit(sub)
scount = 0

for s in subreddit.new(limit=None):
    # title = s.title.lower().split(' ')
    # for word in title:
    #     if word == keyword:
    #         # print(title)
    #         for w in title:
    #             if w not in omit:
    #                 if w.lower() not in words:
    #                     words[w.lower()] = 1
    #                 else:
    #                     words[w.lower()] += 1
    scount += 1
    if keyword in s.title.lower():
        for w in s.title.split(' '):
            if w.lower() not in omit:
                if w.lower() not in words:
                    words[w.lower()] = 1
                else:
                    words[w.lower()] += 1
    if scount % 100 == 0:
        print(scount)

count = 0
for entry in sorted(words, key=words.get, reverse=True):
    if count <= 10:
        # if entry != keyword:
        print(entry, words[entry])
        count += 1
