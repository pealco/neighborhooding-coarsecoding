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
    
    if word in edits_memo:
        return edits_memo[word]
    else:
        substrings = [(word[:i], word[i:]) for i in xrange(len(word))]
        deletes    = [a + b[1:]               for a, b in substrings if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in substrings if len(b) > 1]
        replaces   = [a + c + b[1:]           for a, b in substrings for c in alphabet if b]
        inserts    = [a + c + b               for a, b in substrings for c in alphabet]
        edits = set(deletes + transposes + replaces + inserts)
        edits_memo[word] = known(edits)
        return edits_memo[word]

def known(words):
    """Returns only words that are in the corpus."""
    return [word for word in words if word in bigcorpus]

def known_edits2(word):
    return set(e2 for e1 in edits(word) for e2 in edits(e1) if e2 in bigcorpus)

def main(sep="\t"):
    for word in corpus:
        print sep.join((word, str(len(edits(word))), str(len(known_edits2(word)))))

if __name__ == "__main__":
    
    edits_memo = {}
    known_memo = {}
    corpus    = read_corpus(sys.stdin)
    #bigcorpus = read_corpus(open("thecorpus"))
    bigcorpus = corpus
    alphabet  = "a&@ObdDERfghIiklmnNprsStTUuvwjzZ"
                
    main()