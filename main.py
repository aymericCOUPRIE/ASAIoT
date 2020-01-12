# coding: utf-8

import grovepi
import time
import datetime
import motion_sensor
import light_sensor
import button
import relay


etat_luz = 0
relay.setRelay(etat_luz)
compteur = 0
compteur2 = 0
compteur3 = 0 # pour dire que toutes les heures on eteint la lumiere

while True:
	try:

		value_light = light_sensor.light()
		value_motion = motion_sensor.motion_sensor()
		value_button = button.bouton()

	
		compteur2+=1
		if compteur2 == 5 :
			compteur += 1
			compteur3 += 1 
			compteur2 =0
			print (compteur)
		

		if value_motion:
			compteur = 0
			print("Mouvement detecte")
		

			if etat_luz == 0 : 
				if value_light < 500 :
					print("Allumer la lumiere")
					etat_luz = 1
					relay.setRelay(etat_luz)
					if compteur % 5 == 0 and (compteur / 5) == 3600: # ca fait une heure que le compteur tourne
						print("eteindre lumiere car 1h")
						etat_luz = 0
						relay.setRelay(etat_luz)
				else:
					print("Ne pas allumer la lumiere")

			else :
				if value_light >= 500 : 
					print ("Eteindre la lumiere")
				 	etat_luz = 0
					relay.setRelay(etat_luz)
				else:	
					print("Ne pas eteindre la lumiere")
		else :
			if etat_luz == 1 :
				if compteur > 300: #(5 fois 60)
					print("eteindre la lumiere car pas de mvmnt")
					etat_luz = 0
					relay.setRelay(etat_luz)
					compteur = 0

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


# il manque : la recuperation des donnees,
#au bout d'une heure de lumiere il faut l'eteindre
