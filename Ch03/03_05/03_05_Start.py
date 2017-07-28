# Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time
print(myFile.readline())

# Iterate through each line of a file
myFile.seek(0)
for l in myFile.readlines():
    
    print(l,end="")

myFile.close()