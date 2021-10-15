from machine import Pin
from WTimer import WTof, WTon
import utime


def execute_example():
    led = Pin(25, Pin.OUT)
    t1 = WTof(5000)
    millis = 0
    m_millis = 0
    delta = 0
    state = 0
    start1 = False

    while True:
        millis = utime.ticks_ms()
        delta = millis - m_millis

        if state == 0:
            start1 = True
            state = 10

        t1.run(delta_time=delta, start=start1)

        if state == 10:
            start1 = False
            state = 20

        if t1.getOutput():
            led.value(1)
        else:
            led.value(0)

        m_millis = millis
