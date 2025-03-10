import RPi.GPIO as Io
import time
my_7_segment = [0x3f,
                0x06,
                0x5b,
                0x4f,
                0x66,
                0x6d,
                0x7c,
                0x07,
                0x7f,
                0x6f]

Io.setmode(Io.BCM)
Io.setwarnings(False)

def port(pin):
    if(pin & 0x01 == 0x01):
        Io.setup(13, Io.OUT)
        Io.output(13, 1)
    else:
        Io.setup(13, Io.OUT)
        Io.output(13, 0)        

    if(pin & 0x02 == 0x02):
        Io.setup(6, Io.OUT)
        Io.output(6, 1)
    else:
        Io.setup(6, Io.OUT)
        Io.output(6, 0)

    if(pin & 0x04 == 0x04):
        Io.setup(20, Io.OUT)
        Io.output(20, 1)
    else:
        Io.setup(20, Io.OUT)
        Io.output(20, 0)

    if(pin & 0x08 == 0x08):
        Io.setup(21, Io.OUT)
        Io.output(21, 1)
    else:
        Io.setup(21, Io.OUT)
        Io.output(21, 0)

    if(pin & 0x10 == 0x10):
        Io.setup(16, Io.OUT)
        Io.output(16, 1)
    else:
        Io.setup(16, Io.OUT)
        Io.output(16, 0)

    if(pin & 0x20 == 0x20):
        Io.setup(19, Io.OUT)
        Io.output(19, 1)
    else:
        Io.setup(19, Io.OUT)
        Io.output(19, 0)

    if(pin & 0x40 == 0x40):
        Io.setup(26, Io.OUT)
        Io.output(26, 1)
    else:
        Io.setup(26, Io.OUT)
        Io.output(26, 0)

while True:
    for x in range(10):
        pin = my_7_segment[x]
        port(pin)
    time.sleep(1)