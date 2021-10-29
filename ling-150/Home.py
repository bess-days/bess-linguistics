import time
import sys
import colored
import importlib
import runpy
import subprocess
import os





print('Welcome to Conclass')
time.sleep(1)
print('Conclass is a system to edit English words, similar to how adding certain suffixes or words'
      'can make a definition oposite of the base word or paint words a different way -- the Conclass method'
      'makes words to be literal.')
print(''
      'No ambiguoty of meaning that causes most of our generations struggles and a way to help anxiety')

time.sleep(3)
print('What do you want to do?')
print('1. Try it yourself'
      '2. Learn about phonology')
choice = int(input('Enter the number of where you want to go: '))
if choice == 1:
      print('hi')
      stream = open("restarting.py")
      read_file = stream.read()
      exec(read_file)
if choice == 2:
      print('bye')
