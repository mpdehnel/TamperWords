# TamperWords
Allows users to verify the integrity of downloaded software easily, without having to know what a hash, or a command line is.

TamperWords, Martin Dehnel Jan 2015. GPLv2.
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

Current Usage:
 - Download tamperWords.py and words1.txt
 - `python tamperWords.py <file-to-check>'

