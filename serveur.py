import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement

#/communication avec alexa
@ask.launch
def launch():
    speech_text = 'je me suis connecter a votre domotique'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)
 #/Intent on va les retrouver dans le fichier json d'Alexa c'est nos commande....
@ask.intent('SalonIntent', mapping = {'status':'status'})
def Salon_Intent(status,salon):

    if status in STATUSON:
        execfile('/home/gpio alexa/SalonHaut.py')
	return statement('A votre service, je monte les volet du salon')

    elif status in STATUSOFF:
        execfile('/home/gpio alexa/SalonBas.py')
        return statement('Comme vous voulez, je descend les volets du salon')

    else:
        return statement('desoler ce n est pas possible.')

@ask.intent('SalMangerIntent', mapping = {'status':'status'})
def SalManger_Intent(status,salmanger):

    if status in STATUSON:
        execfile('/home/gpio alexa/SalMangerHaut.py')
	return statement('je monte les volet de la salle a manger')

    elif status in STATUSOFF:
        execfile('/home/gpio alexa/SalMangerBas.py')
        return statement('je descend les volets de la salle a manger')

    else:
        return statement('desoler ce n est pas possible.')

@ask.intent('CuisIntent', mapping = {'status':'status'})
def Cuis_Intent(status,Cuisine):

    if status in STATUSON:
        execfile('/home/gpio alexa/CuisineHaut.py')
	return statement('je monte les volet de la cuisine')

    elif status in STATUSOFF:
        execfile('/home/gpio alexa/CuisineBas.py')
        return statement('je descend les volets de la cuisine')

    else:
        return statement('desoler ce n est pas possible.')

@ask.intent('ChamieIntent', mapping = {'status':'status'})
def Chamie_Intent(status,chamie):

    if status in STATUSON:
        execfile('/home/gpio alexa/ChAmieHaut.py')
	return statement('je monte les volet de la chambre d amie')

    elif status in STATUSOFF:
        execfile('/home/gpio alexa/ChAmieBas.py')
        return statement('je descend les volets de la chambre d amie')

    else:
        return statement('desoler ce n est pas possible.')
    
@ask.intent('ChLorlaieIntent', mapping = {'status':'status'})
def ChLorlaie_Intent(status,chLorlaie):

    if status in STATUSON:
        execfile('/home/gpio alexa/VHlor.py')
	return statement('je monte les volet de la chambre de Lorlaie')

    elif status in STATUSOFF:
        execfile('/home/gpio alexa/VBlor.epy')
        return statement('je descend les volets de la chambre de Lorlaie')

    else:
        return statement('desoler ce n est pas possible.')

@ask.intent('ChParentIntent', mapping = {'status':'status'})
def ChParent_Intent(status,chparent):

    if status in STATUSON:
        execfile('/home/gpio alexa/Chp-haut.py')
	return statement('je monte les volet de votre chambre')

    elif status in STATUSOFF:
        execfile('/home/gpio alexa/Chp-Bas.py')
        return statement('je descend les volets de votre chambre')

    else:
        return statement('desoler ce n est pas possible.')

@ask.intent('ChaufIntent', mapping = {'status':'status'})
def Chauf_Intent(status,chauffage):

    if status in STATUSON:
        execfile('/home/gpio alexa/ChaufOn.py')
	return statement('j allume votre chauffage')

    elif status in STATUSOFF:
        execfile('/home/gpio alexa/ChaufOff.py')
        return statement('j eteinds votre chauffage')

    else:
        return statement('desoler ce n est pas possible.')
            
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
