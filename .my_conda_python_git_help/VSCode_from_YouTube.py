'''

 https://www.youtube.com/watch?v=-nh9rCzPJ20
In this Python Programming Tutorial, we will be learning how to 
set up a Python development environment in VSCode on Windows. 
In this video, we will learn how to install VSCode, 
get the Python extension installed, 
how to change Python interpreters, 
create virtual environments, 
format/lint our code, 
how to use Git within VSCode, how to debug our programs, 
how unit testing works, and more. '''

import sys, requests

print (sys.version)
print (sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

print(greet('Sergey'))

re = requests.get('https://pythonr.blogspot.com')
print(re.status_code)