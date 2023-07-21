#!/usr/bin/env python

###############
# Author : Matthew McCourry
# Contact: github.com/mbmcc
# Title : Collatz Equation runner
# Description : 
# 
# Created : Tue Jul 18 2023
# Last modified : 
###############


### function code ###

def collatz(number):
    number = int(number)
    if number % 2 == 0:
        number = number // 2
        print(str(number))
        return number
    else:
        number = 3 * number + 1
        print(str(number))
        return number


def main():
    value = input("What's your collatz number?\n")
    while value != 1:
        value = collatz(value)



### execution code ###
main()
