#bad_chars = [", :, ;, ,, ., -, +, =, /, \, |, [ ] { } ( ) * ^ &]
import string
import re

def word_count(s):
    y = re.sub(r'[^a-zA-Z \'\n\t\r]', '', s).lower()
    x = y.split()
    wordCount = {}
    for i in x:
        if i not in wordCount:
            wordCount[i] = 1
        else:
            wordCount[i] += 1
    return wordCount
    



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))