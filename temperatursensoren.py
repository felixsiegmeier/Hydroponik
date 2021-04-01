from machine import Pin
import onewire, ds18x20

class TempSensor:
    def __init__(self, data_pin):
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(Pin(data_pin, Pin.IN)))
        self.roms = self.ds_sensor.scan()
        print("Folgende Sensoren wurden gefunden:")
        count = 1
        for n in self.roms:
            print(str(count)+": "+str(n))
            count += 1
        self.ds_sensor.convert_temp()
    
    def get_temp(self, rom):
        temp = self.ds_sensor.read_temp(self.roms[rom-1])
        return(temp)

    def temp_delta(self, delta):
        temp1 = self.get_temp(1)
        temp2 = self.get_temp(2)
        if temp1 - temp2 > delta:
            return True
        else:
            return False


    '''
    def show(self):
        self.oled.fill(0)
        self.oled.text("Temperaturen: ", 0, 5)
        self.oled.text("Tank: " + str(round(self.get_temp(1),1))+" C", 0, 25)
        self.oled.text("Rohr: " + str(round(self.get_temp(2),1))+" C", 0, 45)
        self.oled.show()
    '''
