# Command Line Arguments
import sys

# Print Arguments
print(sys.argv)
print(len(sys.argv))

# Remove Arguments
sys.argv.remove(sys.argv[0])
print(sys.argv)

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        sum+=int(arg)
    except Exception as e:
        print(e)
    
print(sum)