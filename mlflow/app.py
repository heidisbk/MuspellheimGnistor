import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from joblib import dump
import os
import mlflow

# Import dataset
df = pd.read_csv(
    "https://julie-2-next-resources.s3.eu-west-3.amazonaws.com/full-stack-full-time/linear-regression-ft/californian-housing-market-ft/california_housing_market.csv"
)

# X, y split
X = df.drop("MedHouseVal", axis=1)
y = df.MedHouseVal

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


os.environ["AWS_ACCESS_KEY_ID"] = "AKIA3R62MVALEYIZYEIG"
os.environ["AWS_SECRET_ACCESS_KEY"] = "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"


mlflow.set_tracking_uri("votre_uri")


mlflow.sklearn.autolog()

mlflow.set_experiment("Ynov Houssing")

# Get our experiment info
experiment = mlflow.get_experiment_by_name("Ynov Houssing")

with mlflow.start_run(
    experiment_id=experiment.experiment_id, run_name="First training"
):
    # Pipeline
    model = Pipeline(
        steps=[
            ("standard_scaler", StandardScaler()),
            ("Regressor", RandomForestRegressor()),
        ]
    )

    # Entraînement du modèle
    model.fit(X_train, y_train)

    mlflow.log_metric("train_score", model.score(X_train, y_train))

    mlflow.sklearn.log_model(
        model,
        "model houssing",
        registered_model_name="Model houssing",
        artifact_path="model_houssing",
    )


# Print Scores
print(f"Train score: {model.score(X_train, y_train)}")
print(f"Test score: {model.score(X_test, y_test)}")

# Persist our model
print("Saving model...")
dump(model, "./house_prices_model.joblib")
print(f"Model has been saved here: {os.getcwd()}")
