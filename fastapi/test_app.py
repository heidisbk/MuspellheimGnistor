from app import app
from fastapi.testclient import TestClient
from unittest.mock import patch, mock_open
import torch
import torchvision.models as models
from app import download_blob_to_file

client = TestClient(app)


@patch("builtins.open", new_callable=mock_open)
@patch("azure.storage.blob.BlobServiceClient.from_connection_string")
def test_download_blob_to_file(mock_from_connection_string, mock_open):
    # mocks configuration
    mock_blob_service_client = mock_from_connection_string.return_value
    mock_blob_client = mock_blob_service_client.get_blob_client.return_value
    mock_blob_client.download_blob.return_value.readall.return_value = (
        b"Contenu du blob"
    )

    # call test function
    download_blob_to_file("resnet50_1.pt", "./model/resnet50_1.pt", "muspellheim")

    # Assertions
    mock_from_connection_string.assert_called_once_with(
        "DefaultEndpointsProtocol=https;AccountName=heidiynovappd97567;AccountKey=05uRjbMwrelZHIV9RNNGcJZsrjVj9o8xopwVeQODrJuKq7XSe0Z8p30nv1cpqlcXcVQqKUv6KwL2+AStUZk9nA==;EndpointSuffix=core.windows.net"
    )
    mock_blob_service_client.get_blob_client.assert_called_once_with(
        container="muspellheim", blob="resnet50_1.pt"
    )
    mock_blob_client.download_blob.return_value.readall.assert_called_once_with()
    mock_open.assert_called_once_with(file="./model/resnet50_1.pt", mode="wb")
    mock_open.return_value.write.assert_called_once_with(b"Contenu du blob")


def test_num_class_model():
    model_file_path = "./model/resnet50_1.pt"
    model = models.resnet50(num_classes=2, weights=None)
    loaded_weights = torch.load(model_file_path)
    model.load_state_dict(loaded_weights)
    assert model.fc.out_features == 2


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict():
    img_url = "https://github.com/heidisbk/MuspellheimGnistor/blob/dev_traitement_dataset/data_constellations/data_collection/leo/leo0.png?raw=true"
    response = client.get(f"/predict?img_url={img_url}")
    assert response.status_code == 200
    data = response.json()
    assert "Prediction" in data
    assert "Probabilité" in data


def test_predict_with_empty_img_url():
    img_url = ""
    response = client.get(f"/predict?img_url={img_url}")
    assert response.status_code == 422


def test_predict_with_invalid_img_url():
    img_url = "https://github.com/heidisbk/MuspellheimGnistor/blob/dev_traitement_dataset/data_constellations/data_collection/leo/leo0.png"  # Une URL incorrecte
    response = client.get(f"/predict?img_url={img_url}")
    assert "URL is not a valid image" in response.text
