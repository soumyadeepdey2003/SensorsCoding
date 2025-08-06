import time
from Adafruit_ADS1x15 import ADS1115

adc = ADS1115()
GAIN = 1  # Gain = +/- 4.096V

while True:
    try:
        mq2_value = adc.read_adc(0, gain=GAIN)
        print(f"MQ2 Sensor Value: {mq2_value}")
    except Exception as error:
        print(f"Error reading MQ2 sensor: {error}")
    time.sleep(2)
