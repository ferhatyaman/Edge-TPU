from periphery import GPIO
import time

led = GPIO("/dev/gpiochip2", 13, "out")  # pin 37
# button = GPIO("/dev/gpiochip4", 13, "in")  # pin 36

try:
  while True:
    led.write(True)
    time.sleep(2)
    led.write(False)
    time.sleep(2)
finally:
  led.write(False)
  led.close()
  button.close()