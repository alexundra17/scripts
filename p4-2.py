import RPi.GPIO as GPIO
import matplotlib.pyplot as plt 
import numpy as np
from time import sleep
import time
import string 
import math 


def dec2bin(numr, arr):
    return [int(bit) for bit in bin(numr)[2:].zfill(8)]

def bin2dac (v):
    a =[]
    sg = dec2bin(v, a)
    GPIO.output(dac, sg)
    return sg

def LN (num):
    for n in range (0,8):
        GPIO.output(D[n], 0)
    for j in range (7, -1, -1)
        GPIO.output (D[j], num[j])

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2 ** bits
mav_volt = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup (dac, GPIO.OUT, initial = GPIO.LOW)


t = float(input("time"))
f = float(input("frec"))
sam_frec = float(input("sam frec"))
try: 
    
finally:
    
