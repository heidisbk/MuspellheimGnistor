import subprocess
import time

# Commande 1 - Exécute le script Python Flask dans un shell distinct
flask_process = subprocess.Popen(["python", "./flask/app_api.py"])

# Attendre quelques secondes (ajustez si nécessaire)
time.sleep(5)

# Commande 2 - Exécute Uvicorn avec l'application FastAPI dans un autre shell distinct
fastapi_process = subprocess.Popen(["uvicorn", "app:app", "--reload"], cwd="./fastapi/")

# Attendre que les processus se terminent
flask_process.wait()
fastapi_process.wait()
