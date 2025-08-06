import time
from Adafruit_ADS1x15 import ADS1115

adc = ADS1115()
GAIN = 1  # Gain = +/- 4.096V

while True:
    try:
        mq135_value = adc.read_adc(1, gain=GAIN)
        print(f"MQ135 Sensor Value: {mq135_value}")
    except Exception as error:
        print(f"Error reading MQ135 sensor: {error}")
    time.sleep(2)
