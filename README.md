## Overview

I've been looking into using multicast for collectd but need a way to test that multicast traffic will actually get to the correct hosts.

Information about [Multicast addresses](https://en.wikipedia.org/wiki/Multicast_address)
Example [Python code for Multicast](https://pymotw.com/2/socket/multicast.html)


## Quickstart

Run the server (receiver) using the following command

```
/usr/local/bin/python3 multicast-tester.py -s -p 7654 -a 239.0.0.1 -w 10
```

Run the client (sender) using the following command

```
/usr/local/bin/python3 multicast-tester.py -c -p 7654 -a 239.0.0.1 -t 10
```



## C Example Code

I took the C example code from the link below as I was having lots of hassle 
getting the Python to work on MacOS

I'm not 100% sure what fixed it but suspect that `bind('', ...)` might not have 
worked but `bind('0.0.0.0', ...)` does.

Anyway, to sanity-check the Multicast networking I compiled the C code as 
follows

```
gcc -o multicast.app multicast.c
```



## References

* [argparse](https://docs.python.org/2/library/argparse.html)
* [multicast sockets](https://pymotw.com/2/socket/multicast.html)
* [C example code](https://web.cs.wpi.edu/~claypool/courses/4514-B99/samples/multicast.c)
* [Python socket programming](https://realpython.com/python-sockets/)
* [Python struct module](https://docs.python.org/3/library/struct.html#module-struct)
* [Multicast bind](https://stackoverflow.com/questions/10692956/what-does-it-mean-to-bind-a-multicast-udp-socket/29526884)
* [Multicast addressing](https://en.wikipedia.org/wiki/Multicast_address)
* [Connect for UDP sockets](https://erlerobotics.gitbooks.io/erle-robotics-python-gitbook-free/udp_and_tcp/connecting_udp_sockets.html)
* APIs
 * [inet_aton](https://linux.die.net/man/3/inet_aton)
 * [Linux socket headers](http://man7.org/linux/man-pages/man7/ip.7.html)
 * [Python struct formatting](https://docs.python.org/3/library/struct.html#module-struct)
 * [Python low-level sockets](https://docs.python.org/3/library/socket.html)
* [Finding include paths](https://stackoverflow.com/questions/6715454/what-is-the-default-path-for-osx-system-include-files-when-building-a-c-applic)
