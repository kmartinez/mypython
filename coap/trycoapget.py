#!/usr/bin/env python3

from coapthon.client.helperclient import HelperClient

#host = "152.78.65.60"
host = "kubuntu"
port = 5683
path ="xml"

client = HelperClient(server=(host, port))
response = client.get(path)
print(response.pretty_print())
client.stop()
