
**Objectives**
1. **Use the openai.Completion.create method to generate an image from DALL-E.**
2. **Convert the image to grayscale using PIL.**
3. **Resize the image to 256x256 pixels using PIL.**
4. **Save the manipulated image to the local file system.**

Your task is to create a Python script that generates a DALL-E image based on the prompt and then applies a series of transformations to it using PIL.

The prompt should be a function argument  in the function `generate_image(prompt)`.

**The transformations to apply include:**

1. Converting the image to grayscale
2. Resizing the image to 256x256 pixels
3. After applying these transformations,your script should save the image to the local file system. it should be saved under `test_img.png`

Your script should use `openai.Completion.create` to generate a DALL-E response, and the PIL library to manipulate the resulting image.
### Grayscale 
Here is a simple technique to gray scale your image.
Make sure to replace 'your_image.jpg' with the path to your actual image file.

Convert the image to grayscale using the `convert()` method with the 'L' mode:

```python
gray_image = image.convert('L')
```
Optionally, you can save the grayscale image using the `save()` method:
```python
gray_image.save('grayscale_image.jpg')
```
Replace 'grayscale_image.jpg' with the desired filename and extension.

Putting it all together, here's an example:

```python
from PIL import Image

# Open the image
image = Image.open('your_image.jpg')

# Convert to grayscale
gray_image = image.convert('L')

# Save the grayscale image
gray_image.save('grayscale_image.jpg')
```
After running this code, you will have a grayscale version of your image saved as `grayscale_image.jpg`.


{Try it!}(python3 exerc.py 1)
[Click here to refresh your test image](close_file test_img.png panel=1; open_file test_img.png panel=1)


{Check It!|assessment}(code-output-compare-183399101)

|||guidance 
```python
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


```
|||
