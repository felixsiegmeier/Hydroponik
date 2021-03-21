from machine import Pin, I2C
import utime, machine, onewire, time, ds18x20, _thread
from ssd1306 import SSD1306_I2C

oled = SSD1306_I2C(128, 64, I2C(scl=Pin(22), sda=Pin(21)))

def gettemp(temp_pin, rom): # Temperaturen auslesen, rom 1 oder 2 für die beiden Sensoren
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(temp_pin))
    delay = 5
    roms = ds_sensor.scan()
    ds_sensor.convert_temp()
    temp = ds_sensor.read_temp(roms[rom-1])
    return temp

def showoled(temp_pin):
    oled.fill(0)
    oled.text("Temperaturen: ", 0, 5)
    oled.text("Tank: " + str(round(gettemp(temp_pin, 1),1))+" C", 0, 25)
   # oled.text(str(round(gettemp(temp_pin, 1),1)), 45, 25)
    oled.text("Rohr: " + str(round(gettemp(temp_pin, 2),1))+" C", 0, 45)
    oled.show()
