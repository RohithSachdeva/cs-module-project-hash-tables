def hashf(s):
    total = 0

    for c in s:
        #print(c, ord(c)) #ord prints out ascii values
        total += ord(c)
    return total 

#turn a string into a number


print(hashf("Beej"))