import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import torchvision.models as models

resnet = models.resnet50(pretrained=True)

num_classes = 2  # classes
num_features = resnet.fc.in_features
resnet.fc = nn.Linear(num_features, num_classes)

learning_rate = 0.001
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(resnet.parameters(), lr=learning_rate, momentum=0.9)

transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
])

data_dir = '../constellations_preprocessed/'
dataset = datasets.ImageFolder(data_dir, transform=transform)

batch_size = 32
data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=4, pin_memory=True)

num_epochs = 10

for epoch in range(num_epochs):
    running_loss = 0.0
    for images, labels in data_loader:
        # Remise à zéro des gradients
        optimizer.zero_grad()

        # Passage avant du modèle
        outputs = resnet(images)

        # Calcul de la perte
        loss = criterion(outputs, labels)

        # Backpropagation & weights update
        loss.backward()
        optimizer.step()

        # Affichage des informations d'entraînement (optionnel)
        # if (batch_idx + 1) % log_interval == 0:
            # print(f'Epoch [{epoch+1}/{num_epochs}], Step [{batch_idx+1}/{len(data_loader)}], Loss: {loss.item():.4f}')
        epoch_loss = running_loss / len(data_loader)
        print(f"Epoch {epoch+1}/{num_epochs} - Loss: {epoch_loss:.4f}")

    # Évaluation du modèle sur les données de validation (optionnel)
    # with torch.no_grad():

torch.save(resnet.state_dict(), './resnet50_1.pt')
