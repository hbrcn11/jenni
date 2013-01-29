#!/usr/bin/env python
"""
quote.py - Jenni Quote Module
Copyright 2008-10, Michael Yanovich, yanovich.net
Licensed under the Eiffel Forum License 2.

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import random
from modules import unicode as uc


def addquote(jenni, input):
    """.addquote <nick> something they said here -- adds the quote to the quote database."""
    text = input.group(2)
    fn = open("quotes.txt", "a")
    output = uc.encode(text)
    fn.write(output)
    fn.write("\n")
    fn.close()
    jenni.reply("Quote added.")
addquote.commands = ['addquote']
addquote.priority = 'low'
addquote.example = '.addquote'
addquote.rate = 30


def retrievequote(jenni, input):
    """.quote <number> -- displays a given quote"""
    text = input.group(2)
    number = int()
    fn = open("quotes.txt", "r")
    lines = fn.readlines()
    MAX = len(lines)
    fn.close()
    random.seed()
    try:
        number = int(text)
    except:
        number = random.randint(1,MAX)
    k = 1
    for line in lines:
        if k == number:
            jenni.reply("Quote %s of %s: " % (number, MAX) + line)
        k += 1
retrievequote.commands = ['quote']
retrievequote.priority = 'low'
retrievequote.example = '.quote'
retrievequote.rate = 30


def delquote(jenni, input):
    """.rmquote <number> -- removes a given quote from the database. Can only be done by the owner of the bot."""
    if not input.owner: return
    text = input.group(2)
    number = int()
    fn = open("quotes.txt", "r")
    lines = fn.readlines()
    MAX = len(lines)
    fn.close()
    try:
        number = int(text)
    except:
        jenni.reply("Please enter the quote number you would like to delete.")
        return
    newlines = lines[:number-1] + lines[number:]
    fn = open("quotes.txt", "w")
    for line in newlines:
        txt = uc.encode(line)
        if txt:
            fn.write(txt)
            if txt[-1] != "\n":
                fn.write("\n")
    fn.close()
    jenni.reply("Successfully deleted quote %s." % (number))
delquote.commands = ['rmquote', 'delquote']
delquote.priority = 'low'
delquote.example = '.rmquote'
delquote.rate = 30


if __name__ == '__main__':
    print __doc__.strip()
