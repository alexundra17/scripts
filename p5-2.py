import RPi.GPIO as GPIO
import time


def dec2bin(numr):
    return [int(bit) for bit in bin(numr)[2:].zfill(8)]


def bin2dac(v):
    a = []
    sg = dec2bin(v, a)
    GPIO.output(dac, sg)
    return sg


def num2dac(val):
    # print(val)
    sg = dec2bin(val)
    # print(sg)
    GPIO.output(dac, sg)
    return sg


def bin_find(r):
    a = 0
    for i in range(8):
       # print(i)
        time.sleep(0.0007)
        ni = 2**(7-i) + a
        # print('ni')
        # print(ni)
        sg = num2dac(ni)
        voltage = ni/levels * max_volt
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            if ni+a < 256:
                a = ni+a
        if i == 7:
            print("Dig val")
            print(ni)
            print("Voltage")
            print(voltage)


try:
    dac = [26, 19, 13, 6, 5, 11, 9, 10]
    bits = len(dac)
    levels = 2 ** bits
    max_volt = 3.3
    T_mod = 17
    comp = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(T_mod, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(comp, GPIO.IN)

    while True:
        bin_find(1)
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('cleannn')
