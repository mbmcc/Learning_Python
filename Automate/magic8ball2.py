#!/usr/bin/env python

###############
# Author : Matthew McCourry
# Contact: github.com/mbmcc
# Title : Magic 8 Ball 
# Description :with a list
# 
# Created : Thu Jul 20 05:28:30 PM PDT 2023
# Last modified : 
###############

import random


messages = [
        'It is certain',
        'It is decidedly so',
        'Yes definately',
        'Reply hazy, try again',
        'Ask again later',
        'My reply  is no',
        'Outlook no so good',
        'Very doubtful',
        ]

print(messages[random.randint(0, len(messages) - 1)])

