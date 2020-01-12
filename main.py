# coding: utf-8
import grovepi 
import time 
import datetime 
import motion_sensor 
import light_sensor 
import button 
import relay 



etat_luz = 0 #0 pour éteindre la lumière / 1 pour l'allumer 
relay.setRelay(etat_luz) #par défaut éteind la lumière quand le programme est lancé 
compteur = 0 # comtpeur pour calculer 1 heure et éteindre la lumière si aucune activité 
compteur2 = 0 # compteur pour les secondes (comptes le nb d'itérations avec une pause de 0.2s 
compteur3 = 0 # gère la désactivation des capteurs 
actif = False


while True:
	try:
		value_light = light_sensor.light()
		value_motion = motion_sensor.motion_sensor()
		value_button = button.bouton()
        
	        #gestion des timiing / compteur
		compteur2+=1 # compteur de second
		if compteur2 == 5 : # cas ou on a fait 5 * 0.2s Donc 1s
			compteur += 1 #ajoute 1s
			compteur2 = 0 # remise à 0 du compteur de ms
           	 	compteur3 += 1 #ajoute 1s
    
        
        
 	       	#dans le cas ou on active le bouton, on veut "désactiver" les capteurs pendant 1 heure, si on réappui, relancer les capteurs
		if value_button : # cas ou le bouton est activé
            		actif = not actif # inversion du booleen
            		compteur3 = 0
			
			#cas où la lumière est allumée
			if etat_luz :
				etat_luz = 0
				relay.setRelay(etat_luz) # on éteind la lumière
			#cas où la lumière est éteinte
			else :
				etat_luz = 1
				relay.setRelay(etat_luz) # on allume la lumière
                
                
        
	        # on passe dans la boucle seulement si les bouton sont actifs ou le compteur qui mesure le temps d'inutilisation des boutons dépasse 15mn
        	if actif == False or (compteur3 > (15 * 60)) :
           		compteur3 = 0
        
			#cas ou on détecté un mouvement
            		if value_motion:
				compteur = 0 # réinitialise le timer d'inactivtié à 0
                
		                # cas où la lumière est éteinte
                		if etat_luz == 0 :


					# cas où le seuil de luminosité est insuffisant
        			        if value_light < 500 :
        			                etat_luz = 1
                			        relay.setRelay(etat_luz) #allumer la lumière
                        
                			        # ca fait une heure que le compteur tourne
      					        if compteur % 5 == 0 and (compteur / 5) == 3600:
   				                        etat_luz = 0
                        				relay.setRelay(etat_luz) #éteind la lumière
                            
               			
				# cas ou la lumière est allumée
				else :
                       
			                # cas ou la luminosité est plus forte que le seuil définie
					if value_light >= 500 :
                        			etat_luz = 0
                   				relay.setRelay(etat_luz) # on éteind la lumière
                        
            

		#cas ou aucun mouvement est détecté
            	else :
                	if etat_luz == 1 : #si la lumière est allumée
                    		if compteur > 300: #(5 fois 60) # cas ou il y a pas de mouvement pendant plus de 5mn
                        		etat_luz = 0
                        		relay.setRelay(etat_luz) #on éteind la lumière
                        		compteur = 0 # remise du timer à 0
			
		

		time.sleep(0.2)

	except IOError:
		print("Error")


# il manque : la recuperation des donnees, au bout d'une heure de lumiere il faut l'eteindre
