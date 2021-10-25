try:
    import usocket as socket
except:
    import socket

from machine import Pin
import network
import dht
import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'mou'
password = 'mou123456'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

led = Pin(5, Pin.OUT)
sensor = dht.DHT11(Pin(4))