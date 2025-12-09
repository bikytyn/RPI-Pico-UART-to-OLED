from machine import Pin, I2C, UART
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = SSD1306_I2C(128, 32, i2c)

oled.write_cmd(0xA0)
oled.write_cmd(0xC0)

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

buffer = ""

while True:
    data = uart.read()
    if data:
        s = data.decode("utf-8", "ignore")
        buffer += s[-21:]
        oled.fill(0)
        oled.text(buffer, 0, 24)
        oled.show()