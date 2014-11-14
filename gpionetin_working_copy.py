import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

out_pin = 18
in_pin = 23

GPIO.setup(out_pin, GPIO.OUT)
GPIO.setup(in_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
data_to_send = [1, 0, 1, 0, 1, 1, 1, 0]

# received_data = "1"

def receive():
    input_state = GPIO.input(in_pin)
    if input_state:
        print 1
        # received_data = received_data + '1'
    else:
        print 0
        # received_data = received_data + '0'
    # print received_data

def send():
    if counter < len(data_to_send):
        GPIO.output(out_pin, data_to_send[counter])
        ++counter

while True:
    receive()
    send()
    time.sleep(1)
