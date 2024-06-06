from hifive import *
# Connect to WiFi network
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active()
sta_if.active(True)
sta_if.connect('SSID', 'PASSOWRD')
sta_if.isconnected()
#get the network condig
ip=sta_if.ifconfig()
ip=ip[0]
print(ip)
# Create NIC
network.ESP32()

import usocket
addr = usocket.getaddrinfo(ip, 80)[0][-1]

sock = usocket.socket()
sock.bind(addr)
sock.listen()

print('listening on', addr)


while True:
    temp=temperature()
    temp=str(temp)
    html = "<!DOCTYPE html> <html> <head> <title>HiFive Inventor</title> </head> <body> <h1>Temperature = "+temp+"</h1> </p> </body></html>"
    cl = sock.accept()
    cl_sock = cl[0]
    cl_ip = cl[1]
    print('client connected from', cl_ip)
    cl_sock.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl_sock.send(html)
    cl_sock.close()

    
