
import sys, socket


def getipaddrs(hostname):
    '''get a list of IP addresses from a given hostname. This is a standard(forward) lookup.'''
    result = socket.getaddrinfo(hostname, None, 0 ,socket.SOCK_STREAM)
    return [x[4][0] for x in result]


def gethostname(ipaddr):
    '''Get the hostname from a given IP address. This is a reverse look.'''
    return socket.gethostbyaddr(ipaddr)[0]


def check(ipaddr):
    try:
        # First ,do the reverse lookup and get the hostname.
        hostname = gethostname(ipaddr) # could raise socket.herror

        # Now, do a forward lookup on the result from the earlier reverse lookup
        ipaddrs = getipaddrs(hostname)   #could raise socket.gaierror
    except socket.herror, e:
        print "No host names available for %s; this may be noraml." % ipaddr
        sys.exit(0)

    except socket.gaierror, e:
        print "Got hostname %s, but it could not be forward-resolved: %s" % (hostname,str(e))
        sys.exit(1)

    if not ipaddr in ipaddrs:
        print "Got hostname %s,but on forward lookup," % hostname
        print "original IP %s did not appear in IP address list." % ipaddr
        sys.exit(1)

    print "Validated hostname:", hostname

check('127.0.0.1')