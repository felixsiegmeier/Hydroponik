from machine import Pin, I2C
import onewire, ds18x20
from ssd1306 import SSD1306_I2C

class TempSensor:
    def __init__(self, temp_pin, scl_pin, sda_pin):
        self.oled = SSD1306_I2C(128, 64, I2C(scl=Pin(scl_pin), sda=Pin(sda_pin)))
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(Pin(temp_pin, Pin.IN)))
        self.roms = self.ds_sensor.scan()
        print("Folgende Sensoren wurden gefunden: "+str(self.roms))
        self.ds_sensor.convert_temp()
    
    def get_temp(self, rom):
        temp = self.ds_sensor.read_temp(self.roms[rom-1])
        return(temp)

    def show_temp(self):
        self.oled.fill(0)
        self.oled.text("Temperaturen: ", 0, 5)
        self.oled.text("Tank: " + str(round(self.get_temp(1),1))+" C", 0, 25)
        self.oled.text("Rohr: " + str(round(self.get_temp(2),1))+" C", 0, 45)
        self.oled.show()
