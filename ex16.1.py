from sys import argv

script, filename = argv

input(f"If you want to open {filename}, hit ENTER.")

print(f"Opening {filename}...")
file = open(filename)

print(f"Printing {filename} to the command line.\n")
print(file.read())

print(f"\nClosing {filename}...")
file.close()
