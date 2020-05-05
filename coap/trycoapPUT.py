#!/usr/bin/env python3
from CoAPthon3.coapthon.client.helperclient import HelperClient

host = "152.78.65.60"
#host = "iotgate"
port = 5683
path ="basic"

client = HelperClient(server=(host, port))
response = client.put(path,"frombasicput")
print(response.pretty_print())
client.stop()
