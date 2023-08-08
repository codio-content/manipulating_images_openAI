#CODIO SOLUTION BEGIN

import os
import openai
import secret
from PIL import Image
from io import BytesIO
import requests


openai.api_key = secret.api_key
"""
# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

base_image_url = generate_base_image('red apple')


img_data = requests.get(base_image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)

base_image_url = generate_base_image('red apple')
"""
base_image = Image.open('image_name.jpg')
from PIL import Image, ImageOps, ImageFilter

# Manipulate the image properties
def manipulate_image(image, size, aspect_ratio, brightness, contrast, saturation, hue):
    # Resize the image
    new_size = (int(image.width * size), int(image.height * aspect_ratio * size))
    resized_image = image.resize(new_size, Image.ANTIALIAS)

    # Adjust the image properties
    from PIL import ImageEnhance
    enhanced_image = ImageEnhance.Brightness(resized_image).enhance(brightness)
    enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(contrast)
    enhanced_image = ImageEnhance.Color(enhanced_image).enhance(saturation)

    # Adjust hue only if hue is not 0
    if hue != 0:
        # Convert image to HSV
        hsv_image = enhanced_image.convert('HSV')
        # Shift hue value
        hsv_image = hsv_image.point(lambda p: (p + int(256 * hue)) % 256 if p < 256 else p)
        # Convert back to RGB
        enhanced_image = hsv_image.convert('RGB')

    return enhanced_image

# Example of image manipulation with only size change
size_changed_image = manipulate_image(
    base_image, size=0.8, aspect_ratio=1, brightness=1,
    contrast=1, saturation=1, hue=0
)


# Example of image manipulation
manipulated_image = manipulate_image(
    base_image, size=0.8, aspect_ratio=2, brightness=1,
    contrast=1, saturation=1, hue=0
)
# Save the manipulated image to a file
manipulated_image.save('manipulated_red_apple.jpg')

# Example of image manipulation with only size change
size_changed_image = manipulate_image(
    base_image, size=0.2, aspect_ratio=1, brightness=1,
    contrast=1, saturation=1, hue=0
)

# Save the size-changed image to a file
size_changed_image.save('size_changed_red_apple.jpg')


# Example of image manipulation with a more purple hue
purple_image = manipulate_image(
    base_image, size=1, aspect_ratio=1, brightness=1,
    contrast=1, saturation=1, hue=0.8
)

# Save the purple image to a file
purple_image.save('purple_red_apple.jpg')
# CODIO SOLUTION END