# -*- coding: utf-8 -*-
"""
Angela DeLeo
CPSC 223P-01
01/31/2021
atakux707@csu.fullerton.edu
"""

import sys


cmdInput = input() #receive user input

words = cmdInput.split()

#find the length of the minimum word
#set minLength to the length of the user input
minLength = len(cmdInput)
#get the word and length smaller than current minLength (length of input)
for s in words:
    #set counter to 0
    minCount = 0
    for w in s:
        minCount += 1
    #if counter is less than the minLength, we are done
    if (minCount < minLength):
        minLength = minCount
        #set small to be from index 0 to the end of minlength for printing
        small = s[0:minLength]

#find the length of the maximum word
#set maxLength to 0
maxLength = 0
#get the word and length larger than the current maxLength (0)
for l in words:
    #set counter to 0
    maxCount = 0
    for w in l:
        maxCount += 1
    #if counter is greater than the maxLength, we are done
    if (maxCount > maxLength):
        maxLength = maxCount
        #set large to be from index 0 to the end of maxLength for printing
        large = l[0:maxLength]

#print the shortest word and its length
print("Shortest word: ", small)
#if its length is 1 it prints character rather than characters
if minLength == 1:
    print("It is ", minLength, " character")
else:
    print("It is ", minLength, " characters")
    
#print the longest word and its length
print("Longest word: ", large)
print("It is ", maxLength, " characters")

print(sys.argv)