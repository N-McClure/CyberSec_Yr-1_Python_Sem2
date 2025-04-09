# Today we are talking about 'sand-boxing' and other security features.

# Playing around with the 'OS' module:
# ------------------------------------ #

import os # Imports the OS module.

filename = 'test.txt' # Global variable for our test text document.

# TODO: Get the cureent working directory: os.getcwd()
print("The current working directory is: ", os.getcwd())

# TODO: Navigate to a different directory: os.chdir()
os.chdir(r'C:\Users\Nick\Desktop\Python_1\Sem2')
print('After executing the change dir command, current directory is: ', os.getcwd())
print('Navigating back to week12 folder...')
os.chdir(r'C:\Users\Nick\Desktop\Python_1\Sem2\Week12')
print("The current working directory is: ", os.getcwd())

# TODO: Make a directory: os.mkdir()
# os.mkdir('Directory_0')

# TODO: Make a directory structure with subfolders: os.makedirs()
# os.makedirs('Directory_1/f0/f01')

# TODO: List the files and directories: os.listdir()
print(os.listdir())

# TODO: Obtain and display the 'stat' info of a file: os.stat(filename)
print(os.stat('test.txt'))

# TODO: Display file size: os.stat(filename).st_size
print(os.stat('test.txt').st_size)

# TODO: Display file permissions: os.stat(filename.st_mode)
print(os.stat('test.txt').st_mode)

# ===================================================================================== #
print("# ===================================================================================== #")

# Doing more work with manipulating the File Permissions.
# ------------------------------------------------------- #

import os
import stat

status = os.stat(filename) # returns the status of file.
print(f'The status of {filename}: {status}')

# NOTE: st_mode attribute represents the file perm mode bits in Integer value.
print(f'\n File type and file perm mask: {status.st_mode}')

# TODO: Convert the file perm to octal to get the perm info:
print(f'\n File type and file perm mask in Octal: {oct(status.st_mode)}')

# ===================================================================================== #
print("# ===================================================================================== #")

# Working with 'Restricted Python'.
# --------------------------------- #

from RestrictedPython import compile_restricted
from RestrictedPython import safe_globals

# Safe External Code example:
#external_code = """
#def greet():
  #  return 'Hello world!...I am safe!'
#"""

# Dangerous External Code example:
external_code = """
import os
os.listdir('/')
"""


code = compile_restricted(external_code, '<inline>', 'exec')
outputs = {}
exec(code, safe_globals, outputs)
print(outputs['greet']())