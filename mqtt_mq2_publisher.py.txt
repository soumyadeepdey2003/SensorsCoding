import time
import paho.mqtt.client as mqtt
from Adafruit_ADS1x15 import ADS1115

# Initialize ADS1115 ADC
adc = ADS1115()
GAIN = 1  # +/-4.096V

# MQTT Configuration
broker = "localhost"
port = 1883
topic = "sensor/mq2"
client_id = "MQ2_Publisher"

# Initialize MQTT client and connect
client = mqtt.Client(client_id)
client.connect(broker, port)

def read_mq2():
    # Read MQ2 analog value from A0
    value = adc.read_adc(0, gain=GAIN)
    return value

try:
    while True:
        mq2_value = read_mq2()
        print(f"MQ2 Sensor Value: {mq2_value}")
        client.publish(topic, mq2_value)
        time.sleep(2)

except KeyboardInterrupt:
    print("MQ2 MQTT Publisher Stopped.")
    client.disconnect()
