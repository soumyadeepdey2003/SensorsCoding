import time
from datetime import datetime
import board
import busio
import adafruit_bmp280

# Setup I2C for BMP280
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Optional settings
bmp280.sea_level_pressure = 1013.25

# Hardcoded location for testing
location = "Kolkata, India"

while True:
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pressure = bmp280.pressure

        print(f"Time: {current_time}")
        print(f"Location: {location}")
        print(f"Atmospheric Pressure: {pressure:.2f} hPa")
        print("-" * 40)
        
    except Exception as e:
        print("Error reading BMP280 sensor:", e)
    
    time.sleep(2)
