import RPi.GPIO as GPIO
import time

def dec2bin(numr, arr):
    return [int(bit) for bit in bin(numr)[2:].zfill(8)]

def bin2dac (v):
    a =[]
    sg = dec2bin(v, a)
    print ('sg')
    print (sg)
    GPIO.output(dac, sg)
    return sg


dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2 ** bits
mav_volt = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup (dac, GPIO.OUT, initial = GPIO.LOW)
vvv = 255

try: 
    while True:
        for nmbr in range (1, vvv-1): 
            print (nmbr)
            if nmbr>= levels:
                print("u cant do it")
                continue 
            sg = bin2dac (nmbr)
            volt = nmbr / levels * mav_volt
            print(nmbr)
            print (sg)
            print(volt)
            time.sleep(1)
        for nmbr in range (1, vvv-1):     
            if vvv - nmbr>= levels:
                print("u cant do it")
                continue 
            sg = bin2dac (vvv - nmbr+1)
            volt = nmbr / levels * mav_volt
            print(nmbr)
            print (sg)
            print(volt)
            time.sleep(1)
        
except KeyboardInterrupt:
    print ("Value error")
else: 
    print ('I am okey')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('cleannn')

