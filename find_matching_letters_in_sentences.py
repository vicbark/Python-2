# find matching characters in sentences
a=input("Enter the first sentence ")
b=input("Enter the second sentence ")
c="" # here we write the matching letters in sentences / kuda budem zapisivatj sovpodajuwie bukvi
for x in a: # iterate over the line "a" / pereberaem stroku "a"
    if x in b and x not in c: # if the character is in the string "b" but has not yet been added to "c" /
        # esli simvol estj v stroke "b" i ewe ne dobavlen v "c"
        c += x # add character to new line / pri sovpodenie dobavljaem simvol v novuju stroku
print(c) # matching characters / pishem sovpadajuwie simvoli       
