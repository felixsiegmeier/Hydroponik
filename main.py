# Work in progress... 
from oled import Oled
import datenverwalter, time
from pumpencontroller import PumpenController
from lichtcontroller import LichtController
from machine import Pin

display = Oled(21,22)
daten = datenverwalter.Daten()
pumpe = PumpenController(27)
licht = LichtController(32)
ec_led = Pin(16, Pin.OUT)
ec_minimum = 400

def systemtest():
    display.oled_systemtest()
    pumpe.pumpe_steuern(60,1,[1,1])
    licht.licht_steuern(1,10)

def ec_led_steuern(tds_value, minimum):
    if tds_value > minimum:
        ec_led.value(0)
    else:
        ec_led.value(1)

display.oled_welcome()
time.sleep(6)
systemtest()
ec_led.value(1)
time.sleep(30)
display.oled_abgeschlossen()
ec_led.value(0)
time.sleep(6)

while True:
    daten.update_values()
    display.oled_display(OLED_MODUS_COUNTER=daten.get_value("oled_modus"), PAYLOAD=daten.get_oled_payload())
    pumpe.pumpe_steuern(5,daten.get_value("minute"),[daten.get_value("temp_tank"),daten.get_value("temp_rohr")])
    licht.licht_steuern(daten.get_value("licht_modus"),daten.get_value("hour"))
    ec_led_steuern(daten.get_value("ec"), ec_minimum)