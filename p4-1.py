import RPi.GPIO as GPIO

def dec2bin(numr, arr):
    return [int(bit) for bit in bin(numr)[2:].zfill(8)]

def bin2dac (v):
    a =[]
    sg = dec2bin(v, a)
    GPIO.output(dac, sg)
    return sg


dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2 ** bits
mav_volt = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup (dac, GPIO.OUT, initial = GPIO.LOW)


try: 
    while True:
        print ("Please input number, q-exit")
        nmbr = (input())
        if nmbr.isdigit ():
            nmbr = int(nmbr)
            if nmbr>= levels:
                print("u cant do it")
                continue 
            sg = bin2dac (nmbr)
            volt = nmbr / levels * mav_volt
            print(nmbr)
            print (sg)
            print(volt)
        elif nmbr == 'q':
            break 
        else:
            print("u cant do it")
            continue 
except KeyboardInterrupt:
    print ("Value error")
else: 
    print ('I am okey')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('cleannn')

