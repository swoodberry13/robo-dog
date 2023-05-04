    import time
    import machine

    from secrets import Tufts_Wireless as wifi
    import MQTT_CBR as mqtt_CBR

    mqtt_broker = '{0}'
    topic_sub = '{1}'
    topic_pub = '{1}'
    client_id = 'AntTest2'

    mqtt_CBR.connect_wifi(wifi)
    led = machine.Pin(2, machine.Pin.OUT)  # 6 for 2040

    def blink(delay = 0.1):
        led.off()
        time.sleep(delay)
        led.on()
        
    def whenCalled(topic, msg):
        print((topic.decode(), msg.decode()))
        blink()
        time.sleep(0.1)
        blink()
            
    def main():
        fred = mqtt_CBR.mqtt_client(client_id, mqtt_broker, whenCalled)
        fred.subscribe(topic_sub)

        try:
            fred.check()
            blink()
            fred.publish(topic_pub, {2})
        except OSError as e:
            print(e)
            fred.connect()
        except KeyboardInterrupt as e:
            fred.disconnect()
            print('done') 

   
