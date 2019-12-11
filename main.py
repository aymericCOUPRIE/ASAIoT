import grovepi
import time

import motion_sensor
import light_sensor
import button
import relay
etat_luz = 0
relay.setRelay(etat_luz)
while True:
        try:

                value_light = light_sensor.light()
                value_motion = motion_sensor.motion_sensor()
                value_button = button.bouton()


                if value_button :
                        if etat_luz :
                                etat_luz = 0
                                relay.setRelay(etat_luz)
                                print("Eteindre la lumiere car bouton")
                        else :
                                etat_luz = 1
                                relay.setRelay(etat_luz)
                                print("Allumer la lumiere car bouton")


                time.sleep(0.2)
        except IOError:
                print("Error")

