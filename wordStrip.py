import sys

''' Cleans up the 2.5mb word-file and makes it 665kb '''

filename = "words.txt" 
words = set(x.strip().lower() for x in open(filename))
# print len(words): 235886

''' Strip wordsList of words shorter than 3 and longer than 9. 
	Word list is 85983 in length at this point '''
newWords = []
for word in words:
	if len(word) > 3 and len(word) < 9:
		newWords.append(word)

newWords = sorted(newWords)
# print newWords

f = open('words1.txt', 'w')

f.write("\n".join(newWords))
f.close()