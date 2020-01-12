import time
import grovepi

# Connect the Grove Button to digital port D7
# SIG,NC,VCC,GND
button = 7

grovepi.pinMode(button,"INPUT")


def bouton():
       return grovepi.digitalRead(button)
