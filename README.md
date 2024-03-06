# A ecommerce Flet app

An example of a minimal Flet app.

To run the app:

```
flet run [app_directory]

```

Test de l’application Flet sur Android
Commencez à créer des applications mobiles géniales en Python en utilisant uniquement votre ordinateur et votre téléphone portable !

Installez l’application Flet sur votre appareil Android. Vous utiliserez cette application pour voir comment votre projet Flet fonctionne sur un appareil Android.

Get it on Google Play
Pour commencer sur votre ordinateur, vous devez installer Python 3.8 ou une version ultérieure.

IMPORTANT
Votre appareil Android et votre ordinateur doivent être connectés au même réseau Wi-Fi ou local.

Il est recommandé de commencer par la création d’un nouvel environnement virtuel :


<!-- Windows -->
python.exe -m venv .venv
.venv\Scripts\activate.bat

Ensuite, installez le dernier package :flet

pip install flet --upgrade

Assurez-vous que Flet a bien été installé et que l’interface de ligne de commande Flet est disponible en exécutant :PATH

flet --version

Créez un nouveau projet Flet :

flet create my-app
cd my-app

Exécutez la commande suivante pour démarrer le serveur de développement Flet avec votre application :

flet run --android

Un code QR avec l’URL du projet codée s’affichera dans le terminal :


Ouvrez l’application Appareil photo sur votre appareil Android, pointez sur un code QR et cliquez sur URL pour l’ouvrir dans l’application Flet.

Essayez de mettre à jour (par exemple, remplacer un message d’accueil de contrôle) - l’application sera instantanément actualisée sur votre appareil Android.main.pyText

Vous pouvez essayer un exemple Flet plus complexe de l’introduction.

Pour revenir à l’onglet « Accueil », procédez comme suit :

Appuyez longuement n’importe où sur l’écran avec 3 doigts ou
Secouez votre appareil Android.
Vous pouvez également ajouter « manuellement » un nouveau projet en cliquant sur le bouton « + » et en tapant son URL.