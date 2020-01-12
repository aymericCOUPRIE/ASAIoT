import time
import grovepi

# Connect the Grove PIR Motion Sensor to digital port D8
# SIG,NC,VCC,GND
pir_sensor = 8

grovepi.pinMode(pir_sensor,"INPUT")

def motion_sensor():
        # Sense motion, usually human, within the target range
        return grovepi.digitalRead(pir_sensor)
