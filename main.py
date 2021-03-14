from machine import Pin
import time
import onewire
import ds18x20
import _thread

# Pins definieren
temp_pin = Pin(19)

# regelmäßige Messwerte
temp_tank = 0
temp_rohr = 0

def get_temp(): # Temperaturen auslesen -> ermittelt alle 1 Minute die Temperaturen
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(temp_pin))
    delay = 5
    roms = ds_sensor.scan()
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    temp_tank = ds_sensor.read_temp(roms[0])
    temp_rohr = ds_sensor.read_temp(roms[1])

_thread.start_new_thread(get_temp,())