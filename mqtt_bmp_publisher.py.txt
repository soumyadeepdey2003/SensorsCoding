import time
import board
import busio
import adafruit_bmp280
import paho.mqtt.client as mqtt
import json
from datetime import datetime

# Configuration
location = "Lab1"
mqtt_broker = "localhost"  # Change to your MQTT broker IP if needed
mqtt_port = 1883
mqtt_topic = "iot/bmp280"

# Initialize I2C and BMP280 sensor
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Optional: Set sea level pressure if needed
# bmp280.sea_level_pressure = 1013.25

# MQTT Client Setup
client = mqtt.Client()

try:
    client.connect(mqtt_broker, mqtt_port, 60)
except Exception as e:
    print(f"MQTT Connection Failed: {e}")
    exit(1)

while True:
    try:
        pressure = bmp280.pressure  # In hPa
        temperature = bmp280.temperature  # Optional: in °C

        payload = {
            "time": datetime.utcnow().isoformat(),
            "location": location,
            "pressure": round(pressure, 2),
            "temperature": round(temperature, 2)
        }

        client.publish(mqtt_topic, json.dumps(payload))
        print("Published:", payload)

    except Exception as e:
        print(f"Sensor Read Failed: {e}")

    time.sleep(5)
