#!/usr/bin/env python
#
# A script for finding word neighborhood sizes.
#
# Author: Pedro Alcocer
# Last modified: 12 Apr 2009
#
# Edit distance code adapted from Peter Norvig.
# 
# Usage: cat corpus.txt | mapper.py > output.txt
#

import sys

def read_corpus(file):
    """Reads the input file and creates a dictionary with phonetic code as keys."""
    return dict([("".join(line.split()[1:]), None) for line in file])

def edits(word):
    """Finds permutations of _word_ with edit distance 1."""
    substrings = [(word[:i], word[i:]) for i in xrange(len(word))]
    deletes    = [a + b[1:]               for a, b in substrings if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in substrings if len(b) > 1]
    replaces   = [a + c + b[1:]           for a, b in substrings for c in alphabet if b]
    inserts    = [a + c + b               for a, b in substrings for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known(words):
    """Returns only words that are in the corpus."""
    return [word for word in words if word in corpus]
    
def main(sep="\t"):
    for word in corpus:
        print sep.join((word, str(len(known(edits(word))))))

if __name__ == "__main__":
    
    corpus   = read_corpus(sys.stdin)
    alphabet = "a&@ObdDERfghIiklmnNprsStTUuvwjzZ"
                
    main()