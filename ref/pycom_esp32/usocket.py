"""usocket – socket module
This module provides access to the BSD socket interface.

See corresponding CPython module for comparison.

Socket address format(s)
    Functions below which expect a network address, accept it in the format of (ipv4_address, port), where ipv4_address is a string with dot-notation numeric IPv4 address, e.g. "8.8.8.8", and port is integer port number in the range 1-65535. Note the domain names are not accepted as ipv4_address, they should be resolved first using socket.getaddrinfo().
"""

from socket import socket, getaddrinfo, error, timeout, AF_INET, SOCK_STREAM, SOCK_DGRAM, SOCK_RAW, IPPROTO_UDP, IPPROTO_TCP, SOL_SOCKET, SO_REUSEADDR

AF_LORA=160

SOL_LORA=1048325

SO_CONFIRMED=983042
SO_DR=983043
