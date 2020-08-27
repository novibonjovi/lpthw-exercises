from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(
    f"Copying from {from_file} to {to_file}.\nOutput file exists: {exists(to_file)}\nContinue? RETURN for Yes, CTRL-C for No.")
input()

open(to_file, 'w').write(open(from_file).read())
