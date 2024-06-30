# Django_blog
Site de Blog, fait en Django
Site de blog, fait en Django par ICHOU Aymane


Pour lancer le projet, il faut se situer dans le répertoire "multilang_site" où se situe le fichier
manage.py, puis lancer cette commande dans le terminal linux : 

python3 manage.py runserver

Le serveur est normalement lancé sur votre localhost, vous pouvez y accéder en recherchant: 
http://127.0.0.1:8000/articles/

sur votre navigateur de recherche. 

Structure du site : 

La page principale est la page des articles, dans laquelle se situe l'ensemble des articles qui ont été publiés.
Dans le coin, en haut à gauche, il y a un select (liste déroulante) qui permet le choix de la langue, soit français soit anglais. 
L'ensemble des éléments statiques seront traduit, qu'ils soient sur cette page ou situé dans les autres onglets. 

Le site dispose de deux autres onglets : "créer un article" et "chatbot", disponible par le biais de boutons cliquable.

L'onglet "créer un article" redirige vers une nouvelle page qui va permettre à l'utilisateur d'entrer un nouvel 
article de blog, constitué d'un titre, d'un contenu, et d'une date de publication après avoir cliqué sur le bouton d'enregistrement. L'enregistrement reconduit directement à la page principale, mais il y a aussi, dans le coin haut gauche, un bouton "<--" indiquant et permettant un retour la page principale.

L'onglet ChatBot, permet de pouvoir discuter avec une IA. Il y a une entrée de texte et un bouton d'envoi. 
Une fois le message entré, il suffit de cliquer sur le bouton envoyer pour interroger l'api d'openAI. Le chat va permettre de visualiser l'échange des messages avec l'API.
La clé utilisé ne possède plus de crédit, permettant l'échange avec l'API. Dans le cas d'une erreur dans le questionnement de l'API, un message dans le chat est directement retourné avec le message de l'erreur ainsi que son type. Comme dans la page de la création d'article, dans le coin haut gauche, il y a un bouton "<--" indiquant un retour la page principale.

La présentation est terminé, amusez-vous bien ! 
  
