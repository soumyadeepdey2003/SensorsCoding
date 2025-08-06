import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
import json
from datetime import datetime

# Configuration
sensor = Adafruit_DHT.DHT22
pin = 4  # GPIO pin number
mqtt_broker = "localhost"  # Or your MQTT broker IP
mqtt_port = 1883
mqtt_topic = "iot/dht22"

location = "Lab1"

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        payload = {
            "time": datetime.utcnow().isoformat(),
            "location": location,
            "temperature": round(temperature, 2),
            "humidity": round(humidity, 2)
        }
        client.publish(mqtt_topic, json.dumps(payload))
        print("Published:", payload)
    else:
        print("Failed to get reading. Try again!")
    time.sleep(5)
