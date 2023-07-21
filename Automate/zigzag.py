#!/usr/bin/env python

###############
# Author : Matthew McCourry
# Contact: github.com/mbmcc
# Title : zig zag
# Description : <https://automatetheboringstuff.com/2e/chapter3/>
# 
# Created : Wed Jul 19 02:41:17 PM PDT 2023
# Last modified : same
###############

import time, sys


indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indent is increasing or not

try:
    while True: # Main progress loop
        print(' ' * indent, end='')
        print('********')
#         print('********', indent) # Debug
        time.sleep(0.1) # pause for 1/10th of a secondd
        
        if indentIncreasing:
            # Increase the number of spaces
            indent = indent + 1
            
            if indent == 20:
                # Change direction
                indentIncreasing = False
            
        else:
            # Decrease the number of spaces
            indent = indent - 1
            if indent < 1:
                # Change direction
                indentIncreasing = True




except KeyboardInterrupt:
    sys.exit()
