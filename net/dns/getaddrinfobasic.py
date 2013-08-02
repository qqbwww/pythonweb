#!usr/bin/env/ python
# Basic getaddrinfo() basic example - Chapter 4 - getaddrinfobasic.py

import sys, socket

def getresult(url):
    result = socket.getaddrinfo(url, None,0,socket.SOCK_STREAM)
    counter = 0
    for item in result:
        #Print out the address tuple for each item
        print "%-2d: %s" % (counter, item[4])
        counter += 1


#result = socket.getaddrinfo(sys.argv[1], None)
#print result[0][4]

getresult('www.example.com')
getresult('www.baidu.com')