from machine import Pin
import network
import time
from umqtt.simple import MQTTClient
from machine import Pin


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
    print((topic, msg))

def main( server="mqtt.prayerwheel.world",):
    c = MQTTClient("umqtt_client", server)
    print("MQTT connected")
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"prayers/out")
    relay = Pin(5, Pin.OUT)
    while True:
        # Blocking wait for message
        print(c.wait_msg())
        relay.value(1)
        time.sleep(10)
        relay.value(0)



if __name__ == "__main__":
    try:
        do_connect() 
        main()
        print("Main exited, restarting")
    except OSError as e:
        print("Connection failure")
        time.sleep(5)
        machine.reset()
