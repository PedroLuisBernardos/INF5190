<pre>
CODE PERMANENT : BERP01039907
NOM            : Pedro Luis Bernardos
COURRIEL       : kk391035@ens.uqam.ca
</pre>

___________________________________________

CORRECTION PROJET DE SESSION INF5190-A21
========================================

NOTE FINALE :                   /100
----------------------------------------

### Note - Fonctionnalités (115xp) : (/60) ###
<!--METTRE LES COMMENTAIRES SUR LES ERREURS ENTRE LES BALISES PRE-->

### Note - Qualité du projet (/40) ###

---

### A1 - 15xp ###

*Trois listes de données doivent être obtenues à l'aide de requêtes HTTP et leur contenu doit être stocké dans une base de données SQLite. Vous devez organiser la structure de vos données de façon à minimiser le nombre de requêtes faites à la BD pour les fonctionnalités que vous réaliserez dans votre projet. N'hésitez pas à changer la modélisation des données.*

* La base de données SQLite est créée à partir du fichier `db/db.sql`
* Les prochaines méthodes vont se trouver dans le fichier `app/scheduler.py` dans la classe `SetUp`
  * Les trois listes sont téléchargées  dans la méthode `télécharger()`
  * Leur contenu est stocké dans las méthodes `create_piscine_db()`, `create_patinoire_db()` et `create_glissade_db`
  * Le tout est appelé par la méthode `run()`

<pre>

</pre>

### A2 - 5xp ###

*L'importation de données du point A1 est faite automatiquement chaque jour à minuit à l’aide d’un BackgroundScheduler.*

* Le BackgroundScheduler est appelé dans le fichier `app/scheduler.py`, dans la classe `SetUp`, dans la méthode `run()`

<pre>

</pre>

### A3 - 5xp ###

*Le système écoute les requêtes HTTP sur le port 5000. La route « /doc » fait apparaître la documentation de tous les services REST. La documentation est en format HTML, généré à partir de fichiers RAML. Intégrez la fonctionnalité du point A2 à l’application Flask créée au point A3.*

* Le fichier `app/templates/api/doc.html` est généré par la commande:
  ```bash
  make raml
  ```
  Cette documentation est entièrement basée sur le fichier `api.raml`.
* Il est accéssible via la route `/doc`

<pre>

</pre>

### A4 - 10xp ###

*Le système offre un service REST permettant d'obtenir la liste des installations pour un arrondissement spécifié en paramètre. Les données retournées sont en format JSON.</br>Ex. GET /api/installations?arrondissement=LaSalle*

* Ce service a été codé dans le fichier `app/api/routes.py`, dans la méthode `installations_arrondissement()`
* Ce service est accéssible via la route `/api/installations`
* Toute sa documentation est présente ici: `/doc#api_installations_get`

<pre>

</pre>

### A5 - 10xp ###

*Une application JavaScript/HTML permet de saisir un arrondissement à partir d'un formulaire HTML. Lorsque l'utilisateur lance la recherche, une requête asynchrone contenant l'arrondissement saisis est envoyée à la route définie en A4. Lorsque la réponse asynchrone revient, l'application affiche la liste des installations dans un tableau. L'application est disponible sur la page d'accueil du serveur (route « / »).*

* Le fichier HTML qui s'occupe d'afficher le tableau est `app/templates/tableau_installations.html`
* Le fichier JS qui s'occupe de faire la rêquete asynchrone est `app/static/js/arrondissement.js`
* La route `/` a été définie au fichier `app/main/routes.py` dans la méthode `index()`
  * J'ai utilisé WTForms pour mon formulaire et il est présent dans le fichier `app/main/forms.py`
* Une rêquete REST appele une méthode du fichier `app/api/routes.py`
  * `installations_arrondissement()`

<pre>

</pre>

### A6 - 10xp ###

*L'application du point A5 offre un mode de recherche par nom d'installation. La liste de toutes les installations est prédéterminée dans une liste déroulante et l'utilisateur choisira une installation parmi cette liste. Lorsque l'utilisateur lance la recherche, une requête asynchrone est envoyée à un service REST que vous devez créer à cet effet. Lorsque la réponse asynchrone revient, l'application affiche l'information connue sur cette installation.*

* Le fichier HTML qui s'occupe d'afficher l'information sur cette installation est `app/templates/noms_installations.html`
* Le fichier JS qui s'occupe de faire la rêquete asynchrone est `app/static/js/nom_installations.js`
* La route `noms_installations/` est définie au fichier `app/main/routes.py` dans la méthode `noms_installations()`
  * J'ai utilisé WTForms pour mon formulaire et il est présent dans le fichier `app/main/forms.py`
* Une rêquete REST appele une méthode du fichier `app/api/routes.py`
  * `info_nom_installation()`

<pre>

</pre>

### D1 - 15xp ###

*Le système offre un service REST permettant de modifier l'état d'une glissade. Le client doit envoyer un document JSON contenant les modifications à apporter à la glissade. Le document JSON doit être validé avec json-schema.*

* Le service REST permetant de modifier l'état d'une glissade est présent au fichier `app/api/routes.py` aux méthodes `update_glissade_put()` et `update_glissade_patch()`
* JSON-Schema est présent pour valider le document envoyé par le client aux fichiers `schemas/create_glissades.json` et `schemas/update_glissades.json`
* Toute la documentation est présente aux routes `/doc#api_glissade__nom__put` et `/doc#api_glissade__nom__patch`

<pre>

</pre>

### D2 - 5xp ###

*Le système offre un service REST permettant de supprimer une glissade.*

* Le service REST permetant de supprimer une glissade est présent au fichier `app/api/routes.py` à la méthode `delete_glissade(nom)`
* Toute la documentation est présente à la route `/doc#api_glissade__nom__delete`

<pre>

</pre>

### D3 - 20xp ###

*Modifier l'application faite en A5 afin de pouvoir supprimer ou modifier les glissades retournées par l'outil de recherche. L'application doit invoquer les services faits en D1 et D2 avec des appels asynchrones et afficher une confirmation en cas de succès ou un message d'erreur en cas d'erreur. Il faut développer la même fonctionnalité pour les piscines et installations aquatiques.*

* Le fichier `app/static/js/arrondissement.js` a été modifié pour ajouter des icônes de modification et de suppréssion
  * La suppréssion se gère au même fichier dans la méthode `supprimer(url, type_inst)`
  * La modification appelle d'autres ressources dans la méthode `modifier(nom, type_inst)`
    * Le fichier HTML qui s'occupe de la modification est `app/templates/api/modifier.html`
    * Le fichier JS qui s'occupe de faire les rêquetes asynchrones est `app/static/js/update.js`
    * Les formulaires de modification sont présents au fichier `app/api/forms.py`

<pre>

</pre>

### F1 - 20xp ###

*Le système est entièrement déployé sur la plateforme infonuagique Heroku.*

*

<pre>

</pre>

---





# TODO

SUPPRIMER gunicorn REQUIREMENTS.TXTX




todo: ajouter derniere condition patinoire





Pedro 11:36 AM  -> /mnt/c/Users/pedro/Desktop/INF5190/app/api (main)
$style routes.py 
routes.py:95:80: E501 line too long (101 > 79 characters)
routes.py:135:80: E501 line too long (101 > 79 characters)





Error: The select element cannot have more than one selected option descendant unless the multiple attribute is specified.

From line 47, column 6732; to line 47, column 6769

n</option><option selected value="Parc Baldwin">Parc B

Error: The select element cannot have more than one selected option descendant unless the multiple attribute is specified.

From line 47, column 12975; to line 47, column 13012

n</option><option selected value="Parc Baldwin">Parc B







Error: Bad value for attribute action on element form: Must be non-empty.

From line 47, column 1; to line 48, column 27

         ↩<form action="" method="post"↩  class="form" role="form">↩  <in

Warning: The form role is unnecessary for element form.

From line 47, column 1; to line 48, column 27

         ↩<form action="" method="post"↩  class="form" role="form">↩  <in