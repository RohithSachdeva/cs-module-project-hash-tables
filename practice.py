"""
table = [None] * 8

def hashf(s):
    total = 0

    bytes = str(s).encode()

    for b in bytes:
        #print(c, ord(c)) #ord prints out ascii values
        total += b
    return total 

#turn a string into a number


print(hashf("Beej"))
print(hashf("Beje")) #collision ... both returned the same sum

"""
#Terrible hash!

table = [None] * 8

def hashf1(s):
    total = 0

    bytes = str(s).encode()

    for b in bytes:
        #print(c, ord(c)) #ord prints out ascii values
        total += b
    return total

def get_index(s):
    value = hashf1(s)

    return value % len(table)

def put(key, value):
    index = get_index(key)
    table[index] = value

def get(key):
    index = get_index(key)
    value = table[index]
    return value

put("Beej", 3490) #add them into the arraay
put("Goats!", 9999)

print(table)
print(get("Beej")) 