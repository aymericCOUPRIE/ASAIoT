import time
import grovepi
import sendData

# Connect the Grove Switch to digital port D3
# SIG,NC,VCC,GND

#switch = 3
# Connect the Grove Relay to digital port D4
# SIG,NC,VCC,GND

relay = 4
#grovepi.pinMode(switch,"INPUT")
grovepi.pinMode(relay,"OUTPUT")



def setRelay(input):
	sendData.sendData(input)
	grovepi.digitalWrite(relay,input)


def getRelay():
	grovepi.digitalRead(relay)
