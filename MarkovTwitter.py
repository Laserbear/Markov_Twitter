import random
from twitter import *
import time

text = ""
file = open('input.poder')
for line in file:
    for word in line:
        text += word

def count_followers(text):
    old_word = ""
    following_frequencies = {}
    text.lower()
    for word in text.split():
        if (old_word in following_frequencies):
            for array in following_frequencies[old_word]:
                no_process_input = True
                if (word == array[1]):
                    array[0] += 1
                    no_process_input = False
            if (no_process_input):
                following_frequencies[old_word].append([1, word])
        else:
            following_frequencies[old_word] = []
            following_frequencies[old_word].append([1, word])
        old_word = word

    for word in following_frequencies:
        sum = 0
        for array in following_frequencies[word]:
            sum += array[0]
        for array in following_frequencies[word]:
           array[0] /= sum

#   print(following_frequencies)
    return following_frequencies


words = count_followers(text)


random.seed(time.time())

word = ""
tweet = ""
new_word = ""

for i in range(0,1):
    t = Twitter(auth=OAuth("4001032633-TOqB8Rtl88ADmADRRP5eLoEhzgHBvRIeeLPkgEK", "rq9lTJ0AtX5ABqGEUpt2eu115zfrq4ghPtpmVkgeWnFNv",  "citHsiYBgLuClM07qtYtOvDbw", "CPef5rf8kuP3tzXseJSe6JVNtCPMAPecBbDFsDsADBjk620IFU"))
    #printable = ""
    for i in range(0, 20):
        tweet += " " + word
       # printable = (" " + word)
        while (word == new_word):
            for branch in words[word]:
                if (random.randint(0,100) <= branch[0] * 100):
                    new_word = branch[1]
        word = new_word

    print(tweet)
    t.statuses.update(status=tweet)
