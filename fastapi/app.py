# Import FastAPI and Uvicorn
import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException  
import requests
import os
from cv2 import imread, resize
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import torch
import torchvision.models as models
from torchvision import transforms



storage_account_key = "05uRjbMwrelZHIV9RNNGcJZsrjVj9o8xopwVeQODrJuKq7XSe0Z8p30nv1cpqlcXcVQqKUv6KwL2+AStUZk9nA=="
storage_account_name = "heidiynovappd97567"
connection_string = "DefaultEndpointsProtocol=https;AccountName=heidiynovappd97567;AccountKey=05uRjbMwrelZHIV9RNNGcJZsrjVj9o8xopwVeQODrJuKq7XSe0Z8p30nv1cpqlcXcVQqKUv6KwL2+AStUZk9nA==;EndpointSuffix=core.windows.net"
container_name = "muspellheim"

def download_blob_to_file(file_name, file_path, container_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    with open(file=file_path, mode="wb") as sample_blob:
        download_stream = blob_client.download_blob()
        sample_blob.write(download_stream.readall())
file_name = 'resnet50_1.pt' 

if len(os.listdir('./fastapi/model/')) == 0:   
    print('Download model')     
    download_blob_to_file(file_name, './fastapi/model/'+file_name,'muspellheim')


loaded_model = torch.load(f="./fastapi/model/resnet50_1.pt")
model = models.resnet50(num_classes=2,weights=None)
model.load_state_dict(loaded_model)

# Documentation description
description = """

# Documentation Ynov API

*  Méthode Get : /root
*  Méthode Get : /predict
"""

# Documentation tags

tags_metadata = [
    {
        "name": "Méthode Get",
        "description": "Méthode Get : /root",
    },
    {
        "name": "Méthode Post",
        "description": "Méthode Get : /predict",
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


@app.get("/predict", tags=["Méthode Get"])
def predict(img_url: str):
    try:
        open('img.jpeg', 'wb').write(requests.get(img_url).content)
        img = imread('img.jpeg')
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize((256, 256), antialias=True)
        ])

        img_tensor = transform(img).unsqueeze(0)
        model.eval()
        with torch.no_grad():
            output = model(img_tensor)

        _, predicted_idx = torch.max(output, 1)

        dict_value = {'0': 'leo', '1': 'orion'}
        class_predict = dict_value[str(int(predicted_idx > 0.5))]

        probability = torch.softmax(output, dim=1)[0]
        predicted_probability = probability[predicted_idx].item()

        result = {
            "Prediction": str(class_predict),
            "Probabilité": str(predicted_probability)
        }

        return result
    except Exception as e:
        raise HTTPException(status_code=422, detail="URL is not a valid image")


if __name__ == "__main__":
    app.run(port=8000)