import random
import re

inputtext = "This is a test of the emergency broadcast network. This is only a test. This doesn\'t affect you"
newString = re.sub(r'[^a-zA-Z \']', '', inputtext).lower()

print(newString)

def word_Count(s):
    s = re.sub(r'[^a-zA-Z \']', '', inputtext).lower()
    x = s.split()
    wordCount = {}
    for i in x:
        if i not in wordCount:
            wordCount[i] = 1
        else:
            wordCount[i] += 1
    return wordCount
        
print(word_Count("This is a test of the emergency broadcast network. This is only a test. This doesn\'t affect you"))



"""
print('a a\ra\na\ta \t\r\n')

x = ("dogs", "birds", "fish")

#print(random.choice(x))

##x = '":;,.-+=/\\|[]{}()*^&'

x.split()

#print(x.split())
"""
