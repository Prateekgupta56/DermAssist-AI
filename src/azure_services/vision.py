import os
import requests
from dotenv import load_dotenv

# Load keys from your .env file
load_dotenv()

class SkinAnalyzer:
    def __init__(self):
        self.api_key = os.getenv("AZURE_VISION_KEY")
        self.endpoint = os.getenv("AZURE_VISION_ENDPOINT")
        # This is the URL for the Custom Vision prediction API
        self.url = f"{self.endpoint}/customvision/v3.0/Prediction/..." 

    def analyze_image(self, image_path):
        headers = {
            'Prediction-Key': self.api_key,
            'Content-Type': 'application/octet-stream'
        }
        
        with open(image_path, 'rb') as img:
            response = requests.post(self.url, headers=headers, data=img)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to connect to Azure"}
