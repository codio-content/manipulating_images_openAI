import os
import openai
from PIL import Image
import io
import requests
import sys
sys.path.insert(1, '/home/codio/workspace')
import secret
openai.api_key = secret.api_key

# Import the student's function
from exerc import generate_image

def test_generate_image():
    # Call the function with a test prompt
    generate_image("A futuristic cityscape at sunset")

    # Check that the image file has been created
    assert os.path.exists("test_img.png"), "The image file was not created"

    # Open the image and verify its properties
    img = Image.open("test_img.png")

    # Check that the image is grayscale
    assert img.mode == "L", "The image is not grayscale"

    # Check that the image has the correct dimensions
    assert img.size == (256, 256), "The image dimensions are not 256x256"
    
    # If the execution reaches this line, all checks have passed
    print("All checks have passed successfully!")

test_generate_image()
