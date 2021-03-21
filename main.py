from machine import Pin, I2C, RTC
import time, network, utime, machine, urequests
import onewire, uhrzeit
import ds18x20
import _thread
from ssd1306 import SSD1306_I2C
import temperatursensoren as temp

uhrzeit.wificonnect()

# Pins definieren
temp_pin = Pin(19, Pin.IN)
button1_pin = Pin(17, Pin.IN)
button2_pin = Pin(33, Pin.IN)
licht_pin = Pin(32, Pin.OUT)

button_pressed = time.time() #oled_show setzt den Wert von oled_status auf 0, wenn 3min kein Button gedrückt wurde
oled_status = 0 #aus, time, temp, EC, Licht => nimmt 0 - 4 an
licht_status = 0 #aus, 8h, 10h, 12h, 14h, 16h, 18h => nimmt 0 - 6 an
oled_func = [oled_off, uhrzeit.showoled, temp_showoled, ec_showoled, licht_showoled]

def oled_button(arg):
    button_pressed = time.time()
    global oled_status
    if oled_status < 4:
        oled_status += 1
    else:
        oled_status = 0

def oled_show(): # aktualisiert das Display => LOOP
    global oled_status
    global oled_func
    if time.time() - button_pressed > 180:
        oled_status = 0
    oled_func[oled_status]()
    
def temp_showoled(): #wird benötigt, da in die Liste oled_func keine Parameter (in diesem Falle der temp_pin) übergeben werden können
    global temp_pin
    temp.showoled(temp_pin)

def licht_button(arg):
    button_pressed = time.time()
    global oled_status
    if oled_status =! 4:
        oled_status = 4
    global licht_status
    if licht_status < 6:
        licht_status += 1
    else:
        licht_status = 0

def licht_controller(licht_status): # sorgt für das Licht => LOOP
    global licht_pin
    global uhrzeit.hour
    if licht_status > 0 and uhrzeit.hour > 4 and uhrzeit.hour < 11+2*licht_status:
        licht_pin.high()
    else:
        licht_pin.low()

button1_pin.irq(trigger=Pin.IRQ_RISING, handler=oled_button)
button2_pin.irq(trigger=Pin.IRQ_RISING, handler=licht_button)

while True:
    uhrzeit.uhrzeitloop()
    temp.get_temp(temp_pin)
    licht_controller(licht_status)
    oled_show()