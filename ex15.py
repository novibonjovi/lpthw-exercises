# import argv from sys module
from sys import argv

# set script and filename as arguments for opening the script
script, filename = argv

# use function open() to pass file object of 'filename' to variable txt
txt = open(filename)

# print string and content of the file object with its method read()
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
