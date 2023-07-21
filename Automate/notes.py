#!/usr/bin/env python

###############
# Author : Matthew McCourry
# Contact: github.com/mbmcc
# Title : Lists
# Description : <https://automatetheboringstuff.com/2e/chapter3/>
# 
# Created : Wed Jul 19 2023
# Last modified : same
###############

spam = ['cat', 'bat', 'rat', 'elephant']

for i in [0, 1, 2, 3]:
    print(i)

range(4)

list(range(4))

spam = list(range(0, 100, 2))

supplies = ['pens', 'staplers', 'flame-thowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

a = 'AAA'
b = 'BBB'
# swap
a, b = b, a

spam = ['hello', 'hi', 'hey', 'howdy', 'heya']

# Dictionaries
## Key : Value pairs

dictionary = {'name': 'matt', 'species': 'human', 'ancestory': 'Northern European'}

list(dictionary.items())
# [('name', 'matt'), ('species', 'human'), ('ancestory', 'Northern European')]

for k, v in dictionary.items():
    print(k, v)

# Tuples are like lists but are immutable and use parenthisis instead of square brackets