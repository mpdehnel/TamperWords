#!/usr/bin/env python

''' TamperWords, Martin Dehnel Jan 2015. GPLv2.
  Inspired by talks from RWC 2015.
  Basic Idea: Users don't (and should have to) understand what a hash is, 
     or how to generate one of some downloaded software.
  Replace hashes with 6-10 randomly chosen (but always the same per file) dictionary words
     with a similar order of magnitude of entropy, and ask the user to check they're
     the same as the ones listed on the website. Words generated from a SHA-256/512 Hash (transparent to user).

  Display the TamperWords on screen automatically after software (.exe, .msi, .dmg, .app etc.) is downloaded,
      do NOT require the user to do anything.
  Initial setup: Chrome & Firefox Extensions.
  Aim: Full integration with Chrome, Firefox, & other browsers.

  Tasks:
      x Write core engine (word generation from input at the command-line)
      - Write a Chrome/Fx extension to display the words automatically.
      - Allow websites to specify a meta-field such as: 
          <meta name="download-hash" content="d30d93fbf523ae769208b89c2eb10e12e7572df8898af4e602b2cfc657bcdaba">
          <meta name="tamperWords" content="primate subsignation bordar coalitioner ignominiously ecurie">
      - Then get this to compare the content from the meta-field to the hash of the download automatically.

      (sha256("I swear by my pretty floral bonnet, I will end you.") == d30d9...)

  Needs a better name. Suggestions welcome!

  URL for words1.txt: https://www.dropbox.com/s/xljc02i0ezuf5rc/words1.txt
  Full wordlist originally from FreeBSD's /share/dict/words:
  http://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co

 '''

import argparse
import hashlib
from functools import partial as p

def tamperWords(filename, dictionary):
    # Read the file in block by block so as not to destroy memory usage
    blocksize, hasher = 2**16, hashlib.sha256()
    with open(filename, 'rb') as myFile:
        for chunk in iter(p(myFile.read, blocksize), b''):
            hasher.update(chunk)

    # hasher = hashlib.sha512('I swear by my pretty floral bonnet, I will end you.')
    digest = hasher.hexdigest()

    # Split the digest into 8 pieces, 128 bits per piece, and mod out to 64 bits each
    chunks = (digest[(i)*8:(i+1)*8] for i in xrange(8))
    chunks = (int(chunk, 16) % 2**16 for chunk in chunks)
    
    # Load dictionary word list
    with open(dictionary) as f:
        words = f.read().split()

    # Convert 64-bit digest pieces to words. Choosing 0-65535.
    return " ".join(words[chunk] for chunk in chunks)

''' Take filename as input from the command-line '''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="path to file to be digested")
    parser.add_argument("--dictionary", help="optional dictionary to use for string generation", default="words1.txt")
    args = parser.parse_args()

    print tamperWords(args.filename, args.dictionary)

