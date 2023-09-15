# load model with tensorflow
import tensorflow as tf
import mlflow
import os

# Import du model sauvegardé avec Keras
model = tf.keras.models.load_model("model.h5")

os.environ["AWS_ACCESS_KEY_ID"] = "AKIA3R62MVALEYIZYEIG"
os.environ["AWS_SECRET_ACCESS_KEY"] = "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"


mlflow.set_tracking_uri("https://heidi-ynov-mlflow-eaa4a390fee0.herokuapp.com/")

# Création de l'expérience "Model Classification"
mlflow.set_experiment("Model Ynov Classification")


# Début de l'expérience (run name = "First Run")
mlflow.start_run(run_name="Run - save model")

# Sauvegarde du modèle sur MLFlow
mlflow.tensorflow.log_model(
    model=model, artifact_path="model", registered_model_name="model_classification"
)
