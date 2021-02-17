
# coding: utf-8

# In[46]:


'''
Code written in DAT-129 during class session for traversing
an arbitrary file tree on a variety of platforms

Functionality at the end of class was to visit each
directory in a tree, send the list of files within to a method
which then examines each file individually, 
extracts its size, and strips the file extension off
with a regular expression.

Students were encouraged to contiue this project by building
variables to store metrics about the trees, such as 
maximum depth and breadth, average file size, 
total tree size, and so forth.

'''
from zipfile import ZipFile
import os
import re

'''
Uncomment these two lines to test out the extraction of a
zip archive called darien-tree.zip that must be located
in the same directory as this script
'''
# with ZipFile('darien-tree.zip', 'r') as zipObj:
#     zipObj.extractall()

# Utility function for exploring features of a list of files
# discovered from our os.walk method
def interrogateFiles(dirname, fileList):
    # Build the regular expression once, 
    # and store the compiled version for use in the loop
    # We save overhead by compiling only once, and not once
    # for each file we interrogate
    # the (  ) in the regexp create a group
    # which we then mark with $ to instruct the engine
    # to start looking for a match at the right end of the given string
    regexp = re.compile('(\.\w+)$')
    for f in fileList:
        # rebuld the file name from the given directory name
        # and the OS-specific file path separator we can get with os.sep
        # and the filename we get from our iterator
        fn = dirname + str(os.sep) + f
        print('file name: ', fn)
        print('file size: ', end='')
        if os.path.isfile(fn):
            print(os.path.getsize(fn),'B')
            match = re.search(regexp, fn)
            if match:
                print('extension: ', match.group(0))


# In[47]:


# traversing directory tree rooted in my current location    
for loc, dirs, files in os.walk('.'):
    print('visiting location: ', loc)
    # pass the current iteration's object pair (ignoring dirs)
    # to our method dedicated to looking at a list of files 
    # in any arbitrary file location
    interrogateFiles(loc, files)

