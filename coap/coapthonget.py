#!/usr/bin/env python3
# simple test of Coap GET to an ipv6 node (to a RIOT-OS resource)
from coapthon.client.helperclient import HelperClient

host = "2001:db8::204:2519:1801:c6d5"
port = 5683
path ="/riot/board"

client = HelperClient(server=(host, port))
response = client.get(path)
print(response.pretty_print())
client.stop()
