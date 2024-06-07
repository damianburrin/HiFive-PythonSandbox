from hifive import *
import esp32

# Connect to WiFi
# Set the WiFi Mode to 1
esp32.set_wifi_mode(1)
# Change to your WiFi and Password
esp32.connect("SSID", "PASSWORD")

# Function to get the weather of the given city
def get_weather(city):
    esp32.conn_open_tcp("api.openweathermap.org", 80)
    response = esp32.cip_send("GET /data/2.5/weather?q={}&units=metric&appid=XXXXXXXX HTTP/1.0\r\nHost: api.openweathermap.org\r\nConnection: close\r\n\r\n".format(city))
    return response[1]

city = "Lincoln,UK"
weather=get_weather(city)
weather=weather.split("\n")
weather=eval(weather[12])
main = weather['main']
Ctemp=main['temp']
print("Current Temp=",Ctemp,"Degrees Celsius")
Ctemp=str(Ctemp)
display.scroll("Current Temp= "+Ctemp+" Degrees Celsius")
