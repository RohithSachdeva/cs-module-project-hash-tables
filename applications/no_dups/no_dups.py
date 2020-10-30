def no_dups(s):
    cache = {}
    words = []
    s = s.split()
    str1 = " "
    for i in s: #O(n)
        if i not in cache: #O(1)?
            cache[i] =+ 1
      
            
    for (k, v) in cache.items(): #O(1)?
        if v == 1: 
            words.append(k)
    return str1.join(words)
        
        
        
        

    
    
    
    
     
"""
1. Split words in the string
2. Add those values once to the cache or only return those whose count = 1?
3. Return the cache with its values as strings
4. Return Cache[i] + " " ... but pop off the last space?  (rstrip)

Or look at morning example and something to do append array
"""    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))