from machine import Pin, I2C, RTC
import time, network, utime, machine, urequests
import onewire, uhrzeit
import ds18x20
import _thread
from ssd1306 import SSD1306_I2C
import temperatursensoren as temp

# Pins definieren
temp_pin = Pin(19, Pin.IN)
button1_pin = Pin(, Pin.IN)
button2_pin = Pin(, Pin.IN)

def button_press(button):
    button.irq()



while True:
   # uhrzeit.uhrzeitloop()
    #temp.get_temp(temp_pin)
    temp.showoled(temp_pin)
    #uhrzeit.showoled()