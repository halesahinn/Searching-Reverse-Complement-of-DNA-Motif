#Büşra YAŞAR-150114063
#Emine Feyza MEMİŞ-150114077
#Hale ŞAHİN-150116841

import operator
import re
import os
import sys
from os import path
#print("Please enter the input file path :")
#path = input()
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def readFile(file_path):
    path2 = path.relpath(file_path)
    with open(path2) as f:
        text = f.read()
        printText(text)
    
def printText(text):
    # Extract your code into a function and print header for current kmer
    #print("%s\n################################" %name)
    kmers = {}
    
    for i in range(len(text) - k + 1):
       kmer = text[i:i+k]
       if kmer in kmers:
          kmers[kmer] += 1
       else:
          kmers[kmer] = 1

    print ('Inputs: k=%d,x=%d' % (k,x))
    print ('Outputs:')
    print ('%d-mer:\t' % (k))
    i = 0
    occuredKmers = {}
    passAmount = 0
    for kmer, count in kmers.items():
        if count >= x:
            print (kmer)
            occuredKmers[i] = kmer
            i = i + 1
            passAmount = passAmount + 1
    if passAmount == 0:
        print('There is no such %d-mer which appears more than %d times for the input DNA string.'  % (k,x))
            

    print ('Reverse Complement: ')
    j = 0
    reverseComplement = ""
    noReverse = 0
    occurence = 0
    while j < len(occuredKmers):
        kmer = occuredKmers[j]
        reverseKmer = reverse(kmer)
        for base in reverseKmer:
            if base == 'A':
                base = 'T'
            elif base == 'T':
                base = 'A'
            elif base == 'G':
                base = 'C'
            elif base == 'C':
                base = 'G'
            reverseComplement = reverseComplement + base

        for i in range(len(text) - k + 1):
            kmer = text[i:i+k]
            if reverseComplement == kmer:
               occurence = occurence +1
        if occurence > 0:
            print (reverseComplement + ' appearing' + ' %d times' % (occurence))
            noReverse = noReverse + 1
        j = j + 1
        occurence = 0
        reverseComplement=""
    if noReverse == 0:
        print ('There is no reverse complement %d-mers in DNA string.' % (k))
if __name__ == "__main__":
    print("Please enter the k value: ")
    k =int(input())
    print("Please enter the x value: ")
    x =int(input())
    print("Please enter the input file path:")
    file_path = input()
    readFile(file_path)

