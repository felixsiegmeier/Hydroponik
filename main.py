# Work in progress...
import sensors, ecsensor, pumpencontroller, lichtcontroller, oled, temperatursensoren, uhrzeit

sensoren = sensors.Sensors()
konzentration_loesung = ecsensor.EcSensor(XXXXXXXXXXXXXXXXXXXXXXXXXX)
pumpe = pumpencontroller.PumpenController(XXXXXXXXXXXXXXXXXXXXXXXXXX)
oled = oled.Oled(XXXXXXXXXXXXXXXXXXXXXXXXXX)
temp = temperatursensoren.TempSensor(XXXXXXXXXXXXXXXXXXXXXXXXXX)


while True:
    sensoren.update()