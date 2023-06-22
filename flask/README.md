# Application Cat-Dog Classifier

## Téléchargement du projet à partir de GitHub

```bash
git clone https://github.com/Mickevin/cat-dog-classifier

cd Integration-continue-app-flsak
```

#### Installation des dépendances du projet à Docker

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Démarage

    `python app.py`

## Démarage du projet via Docker

```bash
docker run -it -v "$(pwd):/app/" -p 4000:5000  mickevin/cat-dog-classifier 

http://127.0.0.1:4000/
```

## Crédits

[Kévin Duranty](https://xn--kvin-duranty-beb.fr/)

[Thème Bootstrap de référence](https://startbootstrap.com/theme/freelancer)
