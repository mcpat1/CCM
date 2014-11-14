import RPi.GPIO as GPIO
import time
import atexit

GPIO.setmode(GPIO.BCM)

out_pin = 18
in_pin = 23

GPIO.setup(out_pin, GPIO.OUT)
GPIO.setup(in_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
data_to_send = [1, 0, 1, 0, 1, 1, 1, 0]

received_data = []

def receive():
	while len(received_data) < 8:
		input_state = GPIO.input(in_pin)
		if input_state:
			print 1
			received_data.append(1)
		else:
			print 0
			received_data.append(0)
		#print received_data
		time.sleep(1)
		
def makeconnection():
	GPIO.output(out_pin, 1)
	acknowledged = 0
	while not acknowledged:
		acknowledged = GPIO.input(in_pin)
	
def send():
    for out_state in data_to_send:
        GPIO.output(out_pin, out_state)
        print 'Sending ' + str(out_state)
        time.sleep(1)
#def validate():

makeconnection()
send()
time.sleep(1)
receive()
#atexit.register(GPIO.cleanup())
