# check the connection is OK and print signal strength
import serial
import time

serial_name = "/dev/ttyUSB0"
serialport = serial.Serial(serial_name, 9600, timeout=0.5)

# only needed once as its stored on the device
def nbiot_connect():
    apname = "ep.inetd.gdsp"
    serialport.write(b'AT+CEREG=2\r')
    response =  serialport.readlines(None)
    print(response)
    # set to max functionality
    serialport.write(b'AT+CFUN=1\r')
    time.sleep(2)
    response =  serialport.readlines(None)
    print(response)
    serialport.write(b'AT+CGDCONT=0,\"IP\",\"" + apname + "\"\r')
    response = serialport.readlines(None)
    print(response)
    serialport.write(b'AT+COPS=1,2,\"27201\"\r')
    response = serialport.readlines(None)
    print(response)


def nbiot_signal():
    #expect [b'AT+CGATT?\r\n', b'+CGATT:1\r\n', b'\r\n', b'OK\r\n']
    serialport.write(b'AT+CGATT?\r')
    response =  serialport.readlines(None)
    print("connected? " + str(response))
    # [b'AT+CSQ\r\n', b'+CSQ:0,99\r\n', b'\r\n', b'OK\r\n']
    serialport.write(b'AT+CSQ\r')
    response =  serialport.readlines(None)
    print("signal?" + str(response[1]).split(":")[1])

nbiot_signal()
