import time
import board
import busio
import adafruit_pca9685

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

hat.frequency = 60

dc1_channel = hat.channels[15]

dc1_channel.duty_cycle = 0

# Increase brightness:
for i in range(0xffff):
    dc1_channel.duty_cycle = i
 
# Decrease brightness:
for i in range(0xffff, 0, -1):
    dc1_channel.duty_cycle = i

time.sleep(5)