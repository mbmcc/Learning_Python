#!/usr/bin/env python

###############
# Author : Matthew McCourry
# Contact: github.com/mbmcc
# Title : my cats 2
# Description : single variable that contains a list
# 
# Created : Thu Jul 20 05:28:30 PM PDT 2023
# Last modified : 
###############

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

