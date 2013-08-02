#!/usr/bin/env python

import sys, socket

def iptohost(ip):
    try:
        # Perform the lookup
        result = socket.gethostbyaddr(ip)

        # Display the looked-up hostname
        print "Primary hostname:"
        print " " + result[0]

        # Display the list of available addressed that is also returned
        print "\nAddresses:"
        for item in result[2]:
            print " " + item

    except socket.herror,e:
        print "Couldn't look up name:",e

iptohost("127.0.0.1")
