from gps import *
from common import *
from time import sleep
import lcd160cr
lcd = lcd160cr.LCD160CR('X')
def lcdinit():
    lcd.set_orient(lcd160cr.LANDSCAPE)
    #Set the position for text output using lcd.write()
    lcd.set_pos(20,70)
    lcd.set_text_color(lcd.rgb(0, 0, 0), lcd.rgb(255, 255, 255))
    lcd.set_font(1)
    lcd.erase()
    lcd.set_pos(10, 10)
    #Write title to the display
    lcd.set_font(2)
    lcd.write('Glacsweb GPS\r\n')

def printfield(txt,n):
    lcd.set_pos(5,10+n*10)
    lcd.write(txt)

def printserial():
    while(1):
        if gpsuart.any() :
            # its possible to read a stump if we don't wait
            sleep(0.1)
            nmeab = gpsuart.readline()
            if (nmeab == None) or (len(nmeab) < 30):
                continue
            nmea = nmeab.decode("ascii", "replace")
            if(nmea.startswith('$GPGGA')):
                f = nmea.split(',')
                print(f[1],f[2])
            print(nmea)

# running average of all values added
class averagepos:
    def __init__(self):
        self.lat_sum =0.0
        self.lon_sum =0.0
        self.alt_sum =0.0
        self.readings =0.0

    def add(self,lat,lon,alt):
        self.lat_sum += lat
        self.lon_sum += lon
        self.alt_sum += alt
        self.readings += 1
        return(self.lat_sum/self.readings, self.lon_sum/self.readings, self.alt_sum/self.readings)
    def clear(self):
        self.lat_sum = 0
        self.lon_sum = 0
        self.alt_sum = 0
        self.readings = 0

def startreading():
    avpos.clear()

def getGpsReading():
    while(1):
        if gpsuart.any() :
            sleep(0.1)
            nmeab = gpsuart.readline()
            if (nmeab == None) or (len(nmeab) < 30):
                continue
            nmea = nmeab.decode("ascii", "replace")
            try:
                msgtype, location = processGPS(nmea)
                lat,lon,alt,sats = location
                return(location)
            except:
                d('..')
                continue
    
lcdinit()

gpsuart = pyb.UART(6,9600)
gpsuart.init(9600,bits=8,parity=None,timeout=2)
startswitch = pyb.Switch() # onboard sw for now
avpos = averagepos()
nmeab = gpsuart.readline() # throw one line away
while(1):
    
    lat,lon,alt,sats = getGpsReading()
    pyb.LED(4).on() # blue LED
    printfield('%.8f' % lat, 2)
    printfield('%.8f' % lon, 3)
    printfield('%.2f' % alt, 4)
    printfield(sats,5)
    print(lat,lon,alt,sats)

    if startswitch.value() :
        print("starting to average")
        startreading()
    print(avpos.add(lat,lon,alt))
    pyb.LED(4).off()

# Save is pressed - store value at end of points.txt file
#log = open('/sd/points.txt', 'a')
#log.write('\r\n')
#close file
#log.close()
