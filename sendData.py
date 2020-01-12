# coding: utf-8

import os
import datetime

def sendData(data):
	if data :
		data = "Eteind"
	else :
		data = "Allume"
	os.system("curl 'https://docs.google.com/forms/d/1Vk_pPTpE9Ucqd8mbSB3a1v5Khl6iH6zU8k9CJcFC_iY/formResponse?ifq&entry.1418034508='" + data + "'&submit=Submit' > log.txt")
#curl : envoi le nouvel état du relai
# > log.txt : redirige toutes les sorties textes vers un fichier de log
