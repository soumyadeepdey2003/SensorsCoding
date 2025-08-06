import time
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

# Loop to read and print LDR data
while True:
    try:
        light_value = ldr_channel.value       # ADC raw value (0 - 65535)
        voltage = ldr_channel.voltage         # Voltage (0.0 - 3.3V)
        print(f"Light Value: {light_value}    Voltage: {voltage:.2f} V")
    except Exception as e:
        print(f"Error reading LDR: {e}")
    time.sleep(2)
