#!/usr/bin/python3

from googlesearch import search
from colorama import Fore, Back, Style
from fake_useragent import UserAgent
from os import path
import os.path

print ("Version 0.1 by c0deninja      ^__^")
print ("                              (oo)\________")
print ("                              (__)\ ./0day )\/\ ")
print ("                                  ||----w||")
print ("gotr00t?                          ||     ||")
print ("________________________________________________")


ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}

dork = input("Enter Dork: ")
numpage = input("Enter number of links to display: ")
print ("\n")

for url in search(dork, stop=int(numpage), user_agent=str(header)):
    print (url)

print("\n")

print ("Found: {} links".format(numpage))

save = input("Save results to a file (y/n)?: ").lower()
if save == "y":
    dorklist = input("Filename: ")
    f = open(dorklist, 'w')
    for url in search(dork, stop=int(numpage)):
        f.writelines(url)
        f.writelines("\n")
    f.close
    if path.exists(dorklist):
        print ("File saved successfully")
    if not path.exists(dorklist):
        print ("File was not saved")
elif save == "n":
    pass



