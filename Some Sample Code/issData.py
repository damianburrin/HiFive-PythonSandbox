
#DCB##

# Import everything from the hifive library
from hifive import *
import esp32

# Set the WiFi Mode
esp32.set_wifi_mode(1)

# Connect to your WiFi, add in these values!
wifi_name = ""
password = ""
esp32.connect(wifi_name, password)

#host variables
host = "api.open-notify.org"

request = "/astros.json"

# Open a TCP Connection to the Website
esp32.conn_open_tcp(host, 80)
# Send a GET Request
response = esp32.cip_send("GET {0} HTTP/1.0\r\nHost: {1}\r\nConnection: close\r\n\r\n".format(request, host))

#split the data into lines
data=response[1].split('\n')

#evalulate the data on line 9
data = eval(data[9])

#get the crew total
crewTotal=data['number']

#Ensure the number is a strinf
crewTotal=str(crewTotal)
#display Crew total
display.scroll("There are "+crewTotal+ " onboard the ISS")


#make the total an integer
crewTotal=int(crewTotal)
#access the crew names using the people key
names=data['people']
#display the intro text
display.scroll("The crew members are.......")
#create a loop 1 for each crew memmber using the total
for crew in range(crewTotal):
  #print each name using the name key
  display.scroll(names[crew]['name'])
  print(names[crew]['name'])
display.scroll("........Data download complete")
