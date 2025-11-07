import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")

def analyze_image(image_bytes):
    """
    Sends image bytes to Hugging Face API for object recognition.
    """
    url = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    response = requests.post(url, headers=headers, data=image_bytes)
    return response.json()
