from machine import Pin, I2C, RTC
import time, network, utime, machine, urequests
import onewire, uhrzeit
import ds18x20
import _thread
from ssd1306 import SSD1306_I2C
import temperatursensoren as temp

uhrzeit.wificonnect() #Wifi wird für die Zeitabfrage benötigt
oled = SSD1306_I2C(128, 64, I2C(scl=Pin(22), sda=Pin(21)))

#Pins definieren
temp_pin = Pin(19, Pin.IN) #über oneWire für beide Sensoren
button1_pin = Pin(17, Pin.IN, Pin.PULL_DOWN) #oled
button2_pin = Pin(33, Pin.IN, Pin.PULL_DOWN) #licht
licht_pin = Pin(32, Pin.OUT) #zum MOSFET für die Beleuchtung

#Varible
button_pressed = time.time() #oled_show setzt den Wert von oled_status auf 0, wenn 3 min kein Button gedrückt wurde, dies ist der 3-Minuten-Timer
oled_status = 1 #aus, time, temp, EC, Licht => nimmt 0 - 4 an
licht_status = 0 #aus, 8h, 10h, 12h, 14h, 16h, 18h => nimmt 0 - 6 an

#Funktionen
def oled_button(arg): #interrupthandler für den oled_button = button1; ändert den oled_status
    button_pressed = time.time()
    global oled_status
    if oled_status < 4:
        oled_status += 1
    else:
        oled_status = 0

def oled_show(): # aktualisiert das Display anhand von oled_status => LOOP
    global oled_status
    global oled_func
    global button_pressed
    if time.time() - button_pressed > 180:
        oled_status = 0
    oled_func[oled_status]()
    
def temp_showoled(): #wird benötigt, da in die Liste oled_func keine Parameter (in diesem Falle der temp_pin) übergeben werden können
    global temp_pin
    temp.showoled(temp_pin)

def licht_button(arg): #interrupthandler für den licht_button = button2 ; ändert den licht_status
    button_pressed = time.time()
    global oled_status
    if oled_status != 4:
        oled_status = 4
    global licht_status
    if licht_status < 6:
        licht_status += 1
    else:
        licht_status = 0

def licht_controller(): # sorgt für das Licht anhand von licht_status => LOOP
    global licht_status
    global licht_pin
    #global uhrzeit.hour
    if (licht_status > 0) and (uhrzeit.hour > 4) and (uhrzeit.hour < (11+2*licht_status)): #FUNKTIONIERT NOCH NICHT
        licht_pin.value(1)
    else:
        licht_pin.value(0)

def licht_showoled(): #NICHT GETESTET
    oled.fill(0)
    if licht_status != 0:
        oled.text("Lichtstunden: "+str(6+2*licht_status),0,5)
        oled.text("5:00 Uhr bis",0,25)
        oled.text(str(11+2*licht_status)+":00 Uhr",0,45)
    else:
        oled.text("Beleuchtung aus", 0, 40)
    oled.show()
    
def oled_off(): #NICHT GETESTET
    oled.fill(0)
    oled.show()

def ec_showoled():
    pass

button1_pin.irq(trigger=Pin.IRQ_RISING, handler=oled_button) #Interrupt oled_button
button2_pin.irq(trigger=Pin.IRQ_RISING, handler=licht_button) # Interrupt licht_button
oled_func = [oled_off, uhrzeit.showoled, temp_showoled, ec_showoled, licht_showoled] #weil python kein switch case hat "switche" ich durch Funktionen in einer Liste

while True:
    uhrzeit.uhrzeitloop()
    temp.gettemp(temp_pin, 1)
    licht_controller()
    oled_show()
    print("Loop")
