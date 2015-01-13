#!/usr/bin/env python

import sys
import argparse

''' Cleans up the 2.5mb word-file and makes it 665kb '''
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="words file to filter", default="words.txt")
    args = parser.parse_args()
    
    with open(args.filename) as f:
        words = set(x.strip().lower() for x in f)
    # print len(words): 235886
    
    # Strip wordsList of words shorter than 3 and longer than 9. 
    # Word list is 85983 in length at this point
    newWords = sorted(word for word in words if len(word) > 3 and len(word) < 9)
    
    with open('words1.txt', 'w') as f:
        f.write("\n".join(newWords))
