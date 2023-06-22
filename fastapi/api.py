# Import FastAPI and Uvicorn
import uvicorn
import pandas as pd
from typing import Literal, List, Union
from fastapi import FastAPI, File, UploadFile
import requests
import os
import mlflow
from cv2 import imread, resize


os.environ['AWS_ACCESS_KEY_ID'] = "AKIA3R62MVALEYIZYEIG"
os.environ['AWS_SECRET_ACCESS_KEY'] = "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"

mlflow.set_tracking_uri("https://heidi-ynov-mlflow-eaa4a390fee0.herokuapp.com/")

# Load model from mlflow
loaded_model = mlflow.pyfunc.load_model('runs:/83b0bed753b24d389e3b33176031803d/model')


# Documentation description
description = """

# Documentation Ynov API

*  Méthode Get : /square
*  Méthode Post : /images
*  Méthode Get : /predict
*  Méthode Post : /articles
"""

# Documentation tags

tags_metadata = [
    {
        "name": "Méthode Get",
        "description": "Méthode Get : /square",
    },
    {
        "name": "Méthode Post",
        "description": "Méthode Post : /articles",
    },
]

# Create the app object
app = FastAPI(
    title="Ynov API",
    description=description,
    tags_metadata=tags_metadata
)

# Endpoint root - Get
@app.get("/", tags=["Méthode Get"])
async def root():
   return {"message": "Hello World"}

# Endpoint Sqaure - Get
@app.get("/square", tags=["Méthode Get"])
async def square(number: int=9):
    return {"square": number * number}


# Import BaseModel from pydantic # Create BaseModel for the article. # Endpoint articles - Post

from pydantic import BaseModel
class Article(BaseModel):
    title: str
    content: str
    author: Literal["Kevin", "Ornella", "Heidi"] = "Kevin"

# Endpoint images - Post
@app.post("/articles", tags=["Méthode Post"])
async def create_artcle(article: Article):

    df = pd.read_csv("articles.csv")
    data = pd.DataFrame([{
        'id': len(df) + 1,
        "title": article.title,
        "content": article.content,
        "author": article.author
    }])

    df = df.append(data, ignore_index=True)
    df.to_csv("articles.csv", index=False)

    return df.to_json()


# Méthode Post avec UploadFile
@app.post("/images", tags=["Méthode Post"])
async def upload_image(file_name: UploadFile = File(...)):
    return {"filename": file_name.filename}


@app.get("/predict", tags=["Méthode Get"])
def predict(img_url:str='https://www.radiofrance.fr/s3/cruiser-production/2023/01/7fd8aaa3-8215-4749-8a14-67d024af6320/1200x680_chaton-getty-picture-alliance.jpg'):
    
    open('img.jpeg', 'wb').write(requests.get(img_url).content)

    img = resize(imread('img.jpeg'), (250, 250)).reshape(1, 250, 250, 3)/255
    pred = loaded_model.predict(img)[0][0]

    dict_value = {'0': 'Chien', '1': 'Chat'}
    class_predict = dict_value[str(int(pred> 0.5))]
    result = {
        "Prediction" : str(class_predict),
        "Probabilité" : str(pred)
        }

    return result


# Run the server with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4000)
