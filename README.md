# alexa-pi
lier alexa au raspberry et le piloter
Code complet pour piloter un raspberry pi 3b et 3b+ depuis Alexa (amazon)
Prés-requi:

 -raspbian à jour sur le raspberry
 -librairie gpio
 -librairie Flask
 -librairie Adafruit-DHT(pour capteur dht11 ou dht22)
 -ngrock ou (ssh -R 80:localhost:5000 serveo.net => en invite de commande ssh sur l'utilisateur root ou pi )
 - des led brancher sur les sortie gpio du raspberry et panser a mettre un dossier dans "/home" que vous allez nommer "alexa gpio" / dans ce dossier il y auras toute vos commande sortie gpio en python.
Pour la partie Alexa:
 -un compte developpeur Alexa => https://developer.amazon.com 
 -Create Skill , ensuite 
 Skill name : le nom que vous voulez par exemple => raspberry.
 Sélectionner Custom et Provision your own.
 La votre skill est créer maintenant on va la lier au raspberry avec les ordres.
 Aller dans JSON Editor:
  -Drag and drop a .json file => la c'est le fichier Json, donc serveur.json
 et  après Save Model
 Aller a Endpoint 
  selectionner https
  puis copier/coller l'adresse https obtenue par ngork ou ssh.
 et Save Model
 Cliquer sur Build et cliquer sur Build Model, sans cette acte la skill ne fonctionnera pas.
 Maintenant on peut tester....
 Cliquer sur Test et taper ou parler ....
  orde : alexa ouvre serveur .
  reponse 'je me suis connecter a votre domotiqiue'
  odre : ferme le salon
  reponse ' '
 ou 
 
  ordre: alexa lance serveur et ouvre le salon
  reponse: 'A votre service, je monte les volet du salon'
  
 Si vous avez tout bien fait sa doit fonctionner, vous pour ajouter autant d 'Intent que vous voulez , mais il faudra modifier le fichier "serveur.py" et il faudra le faire en une seul foix dans la skill, avant enregistrement .
 
 
