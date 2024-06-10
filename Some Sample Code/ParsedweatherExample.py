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

# Gets the weather from the response text
def parse_weather(data):
    # split on the \n - this puts each new line in a seperate item in a list
    weather=data.split("\n")
    #identify the position in the list that has the data in
    #The data is stored in a JSON file with the same format as a python dictionary
    #searchable
    weather=eval(weather[12])
    
    main = weather['weather'] 
    data=main[0]
    condition=data['description']
    return(condition)
      	

city = "Lincoln,UK"

# Use the get_weather() and parse_weather() to get the weather condition
weather_dat = get_weather(city)
condition = parse_weather(weather_dat)

# Display the weather condition
print(condition)
display.scroll(condition)
