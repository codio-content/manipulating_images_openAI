import os
import openai
import secret
from PIL import Image
import io
from io import BytesIO
import requests

openai.api_key = secret.api_key
# CODIO SOLUTION BEGIN
def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url=response['data'][0]['url']

    # Download the image
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))
    # Apply transformations
    img = img.convert("L")  # Convert to grayscale
    img = img.resize((256, 256))  # Resize to 256x256 pixels
    # Save the image
    img.save("test_img.png")

# CODIO SOLUTION END



