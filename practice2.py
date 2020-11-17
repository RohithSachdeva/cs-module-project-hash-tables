import string
import re

ascii_letters = set(map(ord, string.ascii_letters))
non_letters = ''.join(chr(i) for i in range(256) if i not in ascii_letters)

def word_count(s):
    x = s.translate(non_letters)
    wordCount = {}
    for i in x:
        if i not in wordCount:
            wordCount[i] = 1
        else:
            wordCount[i] += 1
    return wordCount
    
print(word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.'))
