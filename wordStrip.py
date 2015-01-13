#!/usr/bin/env python

import sys
import argparse

#Trie Implementation and search from Steve Hanov, 
#with an added deletion feature
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

    def insert( self, word ):
        node = self
        for letter in word:
            if letter not in node.children: 
                node.children[letter] = TrieNode()

            node = node.children[letter]

        node.word = word

    def delete(self, word):
        node = self
        deletion = None
        for letter in word:
            if (len(node.children) <= 1) and (len(node.children[letter].children) == 0):
                #we're the only child
                del(node.children[letter])
                return
            node = node.children[letter]
        #otherwise we are a prefix of something, delete word
        node.word = None
        

# The search function returns a list of all words that are less than the given
# maximum distance from the target word
def search( word, maxCost ):

    # build first row
    currentRow = range( len(word) + 1 )

    results = []

    # recursively search each branch of the trie
    for letter in trie.children:
        searchRecursive( trie.children[letter], letter, word, currentRow, 
            results, maxCost )

    return results

# This recursive helper is used by the search function above. It assumes that
# the previousRow has been filled in already.
def searchRecursive( node, letter, word, previousRow, results, maxCost ):

    columns = len( word ) + 1
    currentRow = [ previousRow[0] + 1 ]

    # Build one row for the letter, with a column for each letter in the target
    # word, plus one for the empty string at column 0
    for column in xrange( 1, columns ):

        insertCost = currentRow[column - 1] + 1
        deleteCost = previousRow[column] + 1

        if word[column - 1] != letter:
            replaceCost = previousRow[ column - 1 ] + 1
        else:                
            replaceCost = previousRow[ column - 1 ]

        currentRow.append( min( insertCost, deleteCost, replaceCost ) )

    # if the last entry in the row indicates the optimal cost is less than the
    # maximum cost, and there is a word in this trie node, then add it.
    if currentRow[-1] <= maxCost and node.word != None:
        results.append( (node.word, currentRow[-1] ) )

    # if any entries in the row are less than the maximum cost, then 
    # recursively search each branch of the trie
    if min( currentRow ) <= maxCost:
        for letter in node.children:
            searchRecursive( node.children[letter], letter, word, currentRow, 
                results, maxCost )

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

    with open('words1.txt', 'w') as f1:
        f1.write("\n".join(newWords))

    #do all-pairs check on distance
    todelete = len(words) - 2**16;
    print todelete

    trie = TrieNode()
    map(trie.insert, newWords)
    print "Trie built"

    dist = 1
    while todelete > 0:
        for i in range(0,len(newWords)-1):
            if todelete == 0:
                break
            closest = search(newWords[i], dist)
            for j in range(1,len(closest)-1):
                newWords.remove(closest[j][0])
                trie.delete(closest[j][0])
                todelete = todelete - 1
                if todelete%100 == 0:
                    print todelete, "words remaining"
                    if todelete == 0:
                        break
        dist = dist + 1
        print "Increased search distance"

    with open('words2.txt', 'w') as f:
        f.write("\n".join(newWords))

