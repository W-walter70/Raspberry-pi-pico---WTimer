from machine import Pin
from WTimer import WTon
import utime


def execute_example():
    led = Pin(25, Pin.OUT)
    t1 = WTon(1000)
    t2 = WTon(1000)
    millis = 0
    m_millis = 0
    delta = 0
    state = 0
    start1 = False
    start2 = False
    led_on = 0
    while True:
        millis = utime.ticks_ms()
        delta = millis - m_millis
        t1.run(delta_time=delta, start=start1)
        t2.run(delta_time=delta, start=start2)

        if state == 0:
            start1 = True
            state = 10

        if state == 10 and t1.getOutput():
            start1 = False
            led_on = 1
            state = 20

        if state == 20:
            start2 = True
            state = 30

        if state == 30 and t2.getOutput():
            start2 = False
            led_on = 0
            state = 0

        led.value(led_on)
        m_millis = millis
