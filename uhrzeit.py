from machine import Pin, I2C, RTC
import time, network, utime, machine, urequests
import onewire
import ds18x20
import _thread
from ssd1306 import SSD1306_I2C


# user data
ssid = "WLAN-589392" # wifi router name
pw = "1223qwwe" # wifi router password
url = "http://worldtimeapi.org/api/timezone/Europe/Berlin" # see http://worldtimeapi.org/timezones
web_query_delay = 60000 # interval time of web JSON query
retry_delay = 5000 # interval time of retry after a failed Web query
update_time = 0
# initialization

# SSD1306 OLED display
oled = SSD1306_I2C(128, 64, I2C(scl=Pin(22), sda=Pin(21)))


# internal real time clock
rtc = RTC()

# wifi connection
print("Connecting to wifi...")
global wifi
wifi = network.WLAN(network.STA_IF) # station mode
wifi.active(True)
wifi.connect(ssid, pw)

# wait for connection
while not wifi.isconnected():
    pass

# wifi connected
print("IP:", wifi.ifconfig()[0], "\n")

time.sleep(1)
# set timer
update_time = utime.ticks_ms() - web_query_delay
    
# if lose wifi connection, reboot ESP8266
if not wifi.isconnected():
    machine.reset()

# query and get web JSON every web_query_delay ms
if utime.ticks_ms() - update_time >= web_query_delay:

    # HTTP GET data
    response = urequests.get(url)

    if response.status_code == 200: # query success
    
        #print("JSON response:\n", response.text)
        
        # parse JSON
        parsed = response.json()
        datetime_str = str(parsed["datetime"])
        year = int(datetime_str[0:4])
        month = int(datetime_str[5:7])
        day = int(datetime_str[8:10])
        hour = int(datetime_str[11:13])
        minute = int(datetime_str[14:16])
        second = int(datetime_str[17:19])
        subsecond = int(round(int(datetime_str[20:26]) / 10000))
    
        # update internal RTC
        rtc.datetime((year, month, day, 0, hour, minute, second, subsecond))
        update_time = utime.ticks_ms()
        #print("RTC updated\n")

    else: # query failed, retry retry_delay ms later
        update_time = utime.ticks_ms() - web_query_delay + retry_delay

date_str = "Date: {1:02d}/{2:02d}/{0:4d}".format(*rtc.datetime())
time_str = "Time: {4:02d}:{5:02d}:{6:02d}".format(*rtc.datetime())

def uhrzeitloop(): # ermittelt die Uhrzeit, muss in die Endlosschleife
    # generate formated date/time strings from internal RTC
    global date_str
    global time_str
    date_str = "Date: {1:02d}/{2:02d}/{0:4d}".format(*rtc.datetime())
    time_str = "Time: {4:02d}:{5:02d}:{6:02d}".format(*rtc.datetime())

def get_time():
    global date_str
    global time_str
    return ([date_str, time_str])
  
def get_hour():
    return(rtc.datetime()[4])

def get_minute():
    return(rtc.datetime()[5])
