# Work in progress... 
from oled import Oled
import datenverwalter

display = Oled(21,22)
daten = datenverwalter.Daten()

while True:
    daten.update_values()
    display.oled_display(OLED_MODUS_COUNTER=daten.get_value("oled_modus"), PAYLOAD=daten.get_oled_payload())