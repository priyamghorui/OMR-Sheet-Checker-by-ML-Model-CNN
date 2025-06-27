import torch
import torch.nn as nn

class BubbleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 7 * 7, 64), nn.ReLU(),
            nn.Linear(64, 2)  
        )

    def forward(self, x):
        x = self.conv(x)
        x = self.fc(x)
        return x
model = BubbleCNN()
model.load_state_dict(torch.load("bubble_cnn_updated.pth", map_location=torch.device('cpu')))
model.eval()  


import cv2
from torchvision import transforms
from PIL import Image


transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

def classify_bubble_cv2(cv2_img):  
    pil_img = Image.fromarray(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))
    input_tensor = transform(pil_img).unsqueeze(0) 

    with torch.no_grad():
        output = model(input_tensor)
        pred = torch.argmax(output, dim=1).item()

    return pred  