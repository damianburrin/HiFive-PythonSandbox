# Import everything from the hifive library
from hifive import *
import music
import esp32

# Set the WiFi Mode
esp32.set_wifi_mode(1)

# Connect to your WiFi, add in these values!
wifi_name = ""
password = ""
my_id = "2"

print(esp32.connect(wifi_name, password))

to_id = "2"
if my_id == "2":
  to_id = "1"

host = "db-hifive.herokuapp.com"
set_to_dev = "/set" + to_id + "?message=hello"
set_to_dev2 = "/set" + to_id + "?message=music"
get_my_mes = "/get" + my_id

# Open a TCP Connection to the Website
print(esp32.conn_open_tcp(host, 80))

while True:
  
  if button_a.was_pressed():
    # Send a GET Request to message setter
    display.show(Image.YES)
    esp32.cip_send("GET {} HTTP/1.0\r\nHost: {}\r\nConnection: Keep-Alive\r\n\r\n".format(set_to_dev, host))
    print("Sending Hello to Dev "  + to_id)

  if button_b.was_pressed():
    # Send a GET Request to message setter
    display.show(Image.YES)
    esp32.cip_send("GET {} HTTP/1.0\r\nHost: {}\r\nConnection: Keep-Alive\r\n\r\n".format(set_to_dev2, host))
    print("Sending Hello to Dev "  + to_id)
  
  # Send a GET Request to message getter
  display.show("S")
    
  response = esp32.cip_send("GET {} HTTP/1.0\r\nHost: {}\r\nConnection: Keep-Alive\r\n\r\n".format(get_my_mes, host))
  display.show("L")
  
  sleep(1000)
  
  #Extract the message
  message = response[1].split('"message":"')
  message = message[1].split('"')
  print("Message: " + message[0])
  
  # Display on LED Matrix
  if message[0] == "hello":
    display.show(Image.HAPPY)
    sleep(1000)

  if message[0] == "music":
    display.show(Image.HAPPY)
    music.play(music.NYAN)
    sleep(1000)
  
  display.clear()
  sleep(50)
