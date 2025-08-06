import time
import json
import paho.mqtt.client as mqtt
from datetime import datetime
import board
import digitalio
import busio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# SPI and MCP3008 Setup
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)  # Chip Select Pin
mcp = MCP.MCP3008(spi, cs)

# LDR connected to Channel 0 (A0)
ldr_channel = AnalogIn(mcp, MCP.P0)

# MQTT Configuration
location = "Lab1"
mqtt_broker = "localhost"
mqtt_port = 1883
mqtt_topic = "iot/ldr"

client = mqtt.Client()
try:
    client.connect(mqtt_broker, mqtt_port, 60)
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

# Continuous reading and publishing
while True:
    try:
        light_value = ldr_channel.value
        voltage = ldr_channel.voltage

        payload = {
            "time": datetime.utcnow().isoformat(),
            "location": location,
            "light_value": light_value,
            "voltage": round(voltage, 2)
        }

        client.publish(mqtt_topic, json.dumps(payload))
        print("Published:", payload)

    except Exception as e:
        print(f"Error reading LDR or publishing: {e}")

    time.sleep(5)
