# Files and File Writing

# Open a file
myFile = open("scores.txt","w")

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file
print(myFile.name)
print(myFile.mode)

# Write to a file
myFile.write("ABC : 100\nQWE : 99\nTYU : 89")
myFile.close()

# Read the file
myFile = open("scores.txt","r")
print(myFile.read())