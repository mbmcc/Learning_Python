#!/usr/bin/env python

###############
# Author : Matthew McCourry
# Contact: github.com/mbmcc
# Title : Magic 8 ball
# Description : <https://automatetheboringstuff.com/2e/chapter3/>
# 
# Created : Wed Jul 19 02:41:17 PM PDT 2023
# Last modified : same
###############

import random


def get_answer(answer_number):
    
    if answer_number == 1:
        return 'It is certain'
    
    elif answer_number == 2:
        return 'It is certain'
    
    elif answer_number == 3:
        return 'It is certain'
    
    elif answer_number == 4:
        return 'It is certain'
    
    elif answer_number == 5:
        return 'It is certain'
    
    elif answer_number == 6:
        return 'It is certain'
    
    elif answer_number == 7:
        return 'It is certain'
    
    elif answer_number == 8:
        return 'It is certain'
    
    elif answer_number == 9:
        return 'It is certain'
 

def main():
     
     r = random.randint(1,9)
     fortune = get_answer(r)
     print(fortune)


### execution ###
main()
