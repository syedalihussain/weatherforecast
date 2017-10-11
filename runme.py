# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:43:26 2017

@author: hussa
"""
import os

print("Welcome to the Project Assignment")

file_loc = input("Enter something: ")
print ("you entered " + file_loc) 
#os.chdir(file_loc)
print(os.getcwd())
file_name = input("Enter File Name: ")
file = open(file_name, "r")
for line in file:
    print(line)