# Before running script write some text in foo.txt

# Open a file
fo = open("foo.txt", 'r+')
print(f"Name of the file: {fo}")

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line
print(f"Reading {fo}:")
print(fo.read())

# Now truncate remaining file.
print(f"Truncating {fo}.")
fo.truncate()

# Read truncated file again
print("Readin truncated file.")
print(fo.read())

# Close opend file
fo.close()
