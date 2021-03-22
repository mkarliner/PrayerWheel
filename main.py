from machine import Pin
import network
import usocket
import usys
import time
from umqtt.simple import MQTTClient
from machine import Pin


#IMPORTANT request clientID, username and password from info@prayerwheel.world!!!

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('SSID', 'PASSWORD')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    

    

def sub_cb(topic, msg):
    global relay
    print((topic, msg))
    relay.value(1)
    time.sleep(10)
    relay.value(0)

def main( server="mqtt.prayerwheel.world",):
    clientID = "xxxxx"
    print('MQTT start')
    c = MQTTClient(clientID, usocket.getaddrinfo(server, 1883)[0][4][0], user="yyyy", password="zzzzz")
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"prayers/out")
    time.sleep(1)
    print("MQTT connected")
    print("Boo")
    while True:
        c.check_msg()
        if(button.value() == 0):
            print('Publishing prayer')
            c.publish(b'prayers/in', clientID)
            time.sleep(1)
        time.sleep_ms(50)

c = 'asf'
relay = Pin(5, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_UP)

if __name__ == "__main__":
    while True:
        try:
            do_connect() 
            main()
            print("Main exited, restarting")
        except OSError as e:
            usys.print_exception(e)
            time.sleep(5)
#         machine.reset()
