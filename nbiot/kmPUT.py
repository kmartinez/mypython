#!/usr/bin/env python3
import sys
import getopt
import os
import serial
import time
import json

# Remote port  of destination Server
remote_port = "5683"
#iotgate.ecs
remote_ip = "152.78.65.60"
serial_name = "/dev/ttyUSB0"

def nbiot_signal():
    #expect [b'AT+CGATT?\r\n', b'+CGATT:1\r\n', b'\r\n', b'OK\r\n']
    serialport.write(b'AT+CGATT?\r')
    response =  serialport.readlines(None)
    rc = str(response[1]).split(':')[1]
    connected =  '1' in rc
    if connected :
        # [b'AT+CSQ\r\n', b'+CSQ:0,99\r\n', b'\r\n', b'OK\r\n']
        serialport.write(b'AT+CSQ\r')
        response =  serialport.readlines(None)
        signal = str(response[1]).split(":")[1]
        rssicode = int(signal.split(",")[0])
    else:
        rssicode = 0
    return connected, rssicode

def nbiot_checkAT():
    serialport.reset_input_buffer()
    serialport.write(b'AT\r')
    response =  serialport.readlines(None)
    rc = str(response)
    if  'OK' in rc :
        return True
    else:
        return False

def waitforOK():
    count = 10
    while count > 0 :
        ret = serialport.readline()
        if "OK" in str(ret):
            return(True)
        print("waiting for OK")
        #print(ret)
        count -= 1

def waitforprompt():
    count = 10
    while count > 0 :
        ret = serialport.read()
        if ret == '>':
            return(True)
        #print("waiting for >")
        count -= 1

print("openning port")
try:
    serialport = serial.Serial(serial_name, 9600, timeout=3)
except (OSError, serial.SerialException):
    print("failed to open serial port")
serialport.reset_input_buffer()
if not nbiot_checkAT() :
    exit(0)
else:
    print("device connected")
con, sig = nbiot_signal()
if con :
    print("signal strength: %d" % sig)
else :
    print("not connected")
    exit(0)

serialport.write(b'AT+CGATT?\r')
# expect +CGATT:1 if connected
reply = serialport.readline(None)
if "+CGATT:1" in str(reply):
    print("Connected")
waitforOK()
print("create coap context")
serialport.write(b'AT+QCOAPCREATE=56830\r')
#waitforOK()
print( serialport.readlines(None))
print("setting path")
serialport.write(b'AT+QCOAPOPTION=1,11,\"basic\"\r')
#waitforOK()
print(serialport.readlines(None))

# type=0 (CON) 1 (NON)
# method= 1(GET) 3 (PUT)
serialport.write(b'AT+QCOAPSEND=1,3,152.78.65.60,5683\r')
# it will reply > then we can send data ^Z
waitforprompt()
time.sleep(3)
serialport.write(b'message from nbiot\x1A\r' )
# returns payload without the ^Z \r OK\r
print(serialport.readline(None))
time.sleep(2)
print(serialport.readline(None))
#serialport.write("AT+QCOAPDATASTATUS?\r")
# returns +QCOAPDATASTATUS: 0
#print("ACK status: " )
#print(serialport.readlines(None))
#delete the coap context
serialport.write(b'AT+QCOAPDEL\r')
print(serialport.readlines(None))
