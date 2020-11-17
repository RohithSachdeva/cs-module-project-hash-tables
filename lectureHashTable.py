table = [None] * 8

def find_index(key):
    key = str(key)
    total = 0
    for c in key:
        total += ord(c)
    return total % len(table) #it gets some data in as the key .. gets some data out as the index
    
#^^^^ converts any string to ascii values 
#can use the key_bytes function to 

def put(key, value):
    index = find_index(key) #they don't care 
    table[index] = value

def get(key):
    index = find_index(key)
    return table[index]

put(3490, "my value")
put(3492, "my value!")

print(get(3490))

print(table)

