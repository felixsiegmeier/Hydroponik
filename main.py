# Work in progress... 
from oled import Oled
import datenverwalter, time
from pumpencontroller import PumpenController
from lichtcontroller import LichtController

display = Oled(21,22)
daten = datenverwalter.Daten()
pumpe = PumpenController(27)
licht = LichtController(32)

def systemtest():
    display.oled_systemtest()
    pumpe.pumpe_steuern(60,1,[1,1])
    licht.licht_steuern(1,10)

display.oled_welcome()
time.sleep(6)
systemtest()
time.sleep(30)
display.oled_abgeschlossen()
time.sleep(6)

while True:
    daten.update_values()
    display.oled_display(OLED_MODUS_COUNTER=daten.get_value("oled_modus"), PAYLOAD=daten.get_oled_payload())
    pumpe.pumpe_steuern(5,daten.get_value("minute"),[daten.get_value("temp_tank"),daten.get_value("temp_rohr")])
    licht.licht_steuern(daten.get_value("licht_modus"),daten.get_value("hour"))