#!/usr/bin/env python
#
# A script for finding word PFNA hash cache sizes.
#
# Author: Pedro Alcocer
# Last modified: 12 Apr 2009
# 
# Usage: cat corpus.txt | mapper.py | reducer.py > output.txt
#

from string import maketrans, translate
from operator import itemgetter
import sys

def ipa2hash(ipa):
    """Converts ASCII IPA to coarsecode."""
    return clean(ipa.translate(CHAR_TO_CODE))

def clean(input):
    """Removes doubled letters from a string."""
    output = input[0]
    for char in input:
        if output[-1] != char: 
            output += char
    return output

def read_mapper_output(file, sep):
    for line in file:
        word, count = line.rstrip().split(sep, 1)
        yield word, ipa2hash(word), int(count)

def main(sep='\t'):
    data = read_mapper_output(sys.stdin, sep=sep)
    data = sorted(data, key=itemgetter(0))
    
    pfna_sizes = {}
    for _, pfna, _ in data:
        if pfna not in pfna_sizes:
            pfna_sizes[pfna] = 1
        else:
            pfna_sizes[pfna] += 1

    for word, pfna, count in data:
        print sep.join((word, pfna, str(pfna_sizes[pfna]), str(count)))

if __name__ == "__main__":
    CHARS = "a&@oObdDEeRfghIiklmnNprsStTUuvwjzZ"
    CODE  = "AAAAAPPFAAAFPFAAPANNNPAFFPFAAFAAFF"    
    CHAR_TO_CODE = maketrans(CHARS, CODE)
    
    main()
    