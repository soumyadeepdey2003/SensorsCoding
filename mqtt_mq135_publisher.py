import time
import paho.mqtt.client as mqtt
from Adafruit_ADS1x15 import ADS1115

# Initialize ADS1115 ADC
adc = ADS1115()
GAIN = 1  # +/-4.096V

# MQTT Configuration
broker = "localhost"
port = 1883
topic = "sensor/mq135"
client_id = "MQ135_Publisher"

# Initialize MQTT client and connect
client = mqtt.Client(client_id)
client.connect(broker, port)

def read_mq135():
    # Read MQ135 analog value from A1
    value = adc.read_adc(1, gain=GAIN)
    return value

try:
    while True:
        mq135_value = read_mq135()
        print(f"MQ135 Sensor Value: {mq135_value}")
        client.publish(topic, mq135_value)
        time.sleep(2)

except KeyboardInterrupt:
    print("MQ135 MQTT Publisher Stopped.")
    client.disconnect()

