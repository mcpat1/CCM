import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

out_pin = 18
in_pin = 23

GPIO.setup(out_pin, GPIO.OUT)
GPIO.setup(in_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
word = []
data_to_send = [1, 0, 1, 0, 1, 1, 1, 0]

# received_data = "1"
def acknowledge():
	while not GPIO.input(in_pin):
		continue
		
def receive():
	while len(word) != 8: 
	    input_state = GPIO.input(in_pin)
    	if input_state:
        	print 1
        	word.append(1)
    	else:
        	print 0
        	word.append(0)
		time.sleep(1)
    # print received_data

def send():
    for out_state in word:
        GPIO.output(out_pin, out_state)
        print 'Sending ' + str(out_state)
        time.sleep(1)
#    if counter < len(data_to_send):
 #       GPIO.output(out_pin, data_to_send[counter])
  #      ++counter
#	
	acknowlegde()
	receive()
    send()
    time.sleep(1)
	
