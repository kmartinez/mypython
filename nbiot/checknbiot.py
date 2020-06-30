# check the connection is OK and print signal strength code
# don't need to do _connect if the unit is already happy
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

con, sig = nbiot_signal()
if con :
    print("signal strength: %d" % sig)
else :
    print("not connected")
