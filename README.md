# MuspellheimGnistor
# Projet de Reconnaissance de Constellations

Ce projet vise à développer un système de reconnaissance de constellations à l'aide de techniques de machine learning. Le but est de permettre l'identification automatique des constellations à partir d'images astronomiques.

## Installation

1. Clonez ce dépôt GitHub sur votre machine locale.
2. Assurez-vous d'avoir Python 3.x installé.
3. Installez les dépendances en exécutant la commande suivante :

```shell
pip install -r requirements.txt
```

## Utilisation

1. Ouvrez le dossier MuspellheimGnistor dans Visual Studio Code.
2. Exécutez le script `run_app.py` pour démarrer le programme de reconnaissance.
3. Aller ensuite sur la première url contenue dans le terminal.
4. Une fois la page web ouverte, entrez l'url d'une image puis cliquer sur le bouton "Lancez la prédiction" pour que l'application fonctionne.

## Structure du Projet

Le projet est organisé de la manière suivante :

- `schema fonctionnel` : schéma décrivant le fonctionnement de l'application.
- `data_constellations/` : dossier contenant les jeux de données (images) utilisés pour l'entrainement du modèle.
- `flask/`
- `fastapi/`
- `mlflow/`
- `muspellheim/`
  - `train.py` : entraînement du modèle.
  - `utils.py` : module contenant des fonctions utilitaires pour le traitement des images et le fonctionnement du modèle.
  - `data_processing.py` : module contenant les fonctionnalités de détection et de reconnaissance de constellations.
  - `requirements.txt`

## License

Ce projet est sous licence [MIT](LICENSE), ce qui signifie que vous êtes libre de l'utiliser, de le modifier et de le distribuer. Toutefois, nous ne sommes pas responsables des éventuels dommages causés par son utilisation.
