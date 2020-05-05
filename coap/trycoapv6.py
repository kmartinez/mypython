#!/usr/bin/env python3

from coapthon/coapthon.client.helperclient import HelperClient

host = "2001:630:d0:f111::4"
#host = "iotgate"
port = 5683
path ="xml"

client = HelperClient(server=(host, port))
response = client.get(path)
print(response.pretty_print())
client.stop()
