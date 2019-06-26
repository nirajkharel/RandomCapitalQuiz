'''
# Program that shows the work of os.path.join() function which return a string with a file path
import os 
haha = os.path.join('usr', 'bin', 'spam')
print(haha)
'''

'''
# Program which combines extra files withe the directory using os.path.join() function
import os
myFiles = ['accounts.txt', 'details.txt', 'invite.txt']
for filename in myFiles:
	print(os.path.join('usr', 'bin', filename))
'''

'''
# Program which shows and change the current working directory
# First the cwd is shown using os.getcwd() and changed using os.chdir() method.
import os
print(os.getcwd())
os.chdir('/usr/bin')
print(os.getcwd())
'''

'''
# Creating New Folders with os.makedirs()
# It creates any necessary intermediate folders of all full paths.
import os
os.makedirs('/home/numb/Niraj/Kharel/is/good/okay')
'''


'''
# Handling absolute and relative paths
# os.path.abspath(path) : returns a string of the absoulte path of the argument
# os.path.isabs(path) : returns True if the argument is an absolute path and False if relative path
# os.path.repath(path, start) : returns a string of a relative path from start path to path
import os
os1 = os.path.abspath('.')
print(os1)
os2 = os.path.abspath('./niraj')
print(os2)
os3 = os.path.isabs('.')
print(os3)
os4 = os.path.isabs(os.path.abspath('.'))
print(os4)
'''


'''
# Program for basename(), dirname() and split() function
# basename() : returns the string of everything that comes after last slash
# dirname() : returns the string of everything that comes before last slash
# split() : returns both strings as a tuple
# os.path.sep() : returns the separated path for each directory in a list 
import os
path = '/home/numb/Niraj/Kharel/niraj.jpg'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(path.split(os.path.sep))
'''


'''
# Finding the size and folder contents
# os.getsize(path) : returns the size in byte of the file
# os.listdir(path) : returns a list of filename strings for each file
# To find the total size of the files in directory, os.path.getsize() and os.listdir() are used together
import os
print(os.path.getsize('/home/numb/Niraj/Kharel/niraj.jpg'))
print(os.listdir('/home/numb/Niraj/Kharel'))
# For total size
total = 0
for filename in os.listdir('/home/numb/Niraj/Kharel'):
	total = total+os.path.getsize(os.path.join('/', 'home', 'numb', 'Niraj', 'Kharel', filename))

print(total)
'''


'''
# This program checks the path validity
# os.path.exists(path) : returns True if path exits and and returns False if do not
# os.path.isfile(path) : returns True if the path argument exists and is a file and return false otherwise
# os.path.isdir(path)  : returns True if path argument exists ans is a folder and return false otherwise
import os
# os.path.exists(path)
print(os.path.exists('C:\\Windows')) # window directory doesnot exits on linux
print(os.path.exists('/home/numb/Niraj/Kharel'))
# os.path.isfile(path)
print(os.path.isfile('/home/numb/Niraj/Kharel')) # returns false
print(os.path.isfile('/home/numb/Niraj/Kharel/niraj.jpg')) # returns True
# os.path.isdir(path)
print(os.path.isdir('/home/numb/Niraj/Kharel')) # return True
print(os.path.isdir('/home/numb/Niraj/Kharel/niraj.jpg')) # returns false
'''


'''
# Program for File Reading and Writing process
test = open('test.txt')
helloContent = test.readlines()
print(helloContent)
'''


'''
# This program is for saving variables with the shelve module
# Storing the variable in a file
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

# Retriving information from the file using shelve module
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])

print(list(shelfFile.keys()))

print(list(shelfFile.values()))
shelfFile.close()
'''


# Progam for saving variable with the pprint.pformat() Function
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
hello = pprint.pformat(cats)
print(hello)
fileobj = open('myCats.py', 'w')
hi = fileobj.write('cats = ' + pprint.pformat(cats) + '\n')
print(hi)
fileobj.close()

import myCats
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0][''])