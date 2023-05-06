#!/usr/bin/env python3

# Lecture 184: How to Debug Code
# debugging

# linting: 
# allows us to detect as we code some issues with our code, formating, read errors
# 
# IDE pycharm has a linting by default
# On VS Code we must install a extension

# pdb
import pdb

def add(num1, num2):
    # print(num1, num2) # hard debugging
    # instead we can use the pdb: gives a interactive python debugger
    # that we can now type commands e.g., type num1, num2, step, help, exit
    print("Hello World!\n")
    pdb.set_trace() 
    t = 4 * 5
    return num1 + num2
    

add(4, 'asdfr')


# def myFunction():
#     print("Hello from my function")

# if __name__ == "__main__":
#     myFunction()
