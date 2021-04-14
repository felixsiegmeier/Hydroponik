# Work in progress... 
from temperatursensoren import TempSensor
import button
from oled import Oled
from ecsensor import EcSensor
import uhrzeit

temp = TempSensor(19)
tank = 1
rohr = 2
buttons = button.Button(17,33,4,X,4)
display = Oled(21,22)
ec = EcSensor(26,34,2000,4095,0)
uhrzeit.wificonnect()

oled_payload = [False,temp.get_temp(tank,rohr),ec.get_ec(temp.get_temp(tank)),uhrzeit.get_time(),buttons.get_licht_modus()]



while True:
    uhrzeit.uhrzeitloop()
    display.oled_display(OLED_MODUS_COUNTER=buttons.get_oled_modus(), PAYLOAD=oled_payload[buttons.get_oled_modus()])
