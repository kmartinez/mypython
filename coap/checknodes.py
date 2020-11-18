#!/usr/bin/env python3
# quick coap GET of a RIOT-OS coap node to see if it is connected OK
# not using coapthon3 as that has some wierd issues
import time
import subprocess as sub
import os
import datetime

nodelist = ["sam1", "sam2", "sam3"]
def getcoap(ip):
    url = "coap://" + ip + "/riot/board"
    result = sub.run(["coap-client","-B 2 -m get ", url], capture_output=True)
    if( result.stdout != b''):
        return(result.stdout)
    else:
        return(0)

while True:
    for node in nodelist :
        if getcoap(node) != 0 :
            ts = datetime.datetime.now().strftime("%Y/%m/%d,%H:%M:%S, ")
            print(ts + " " + node + ' OK')
    time.sleep(10)
