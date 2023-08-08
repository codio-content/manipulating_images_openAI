### PIL

**PIL** (Python Imaging Library) is a popular third-party library used for working with images in Python. It provides a wide range of functions to handle different image processing tasks, such as opening and saving images in various file formats, cropping and resizing images, applying filters and transformations, and much more. In this module, we will use the PIL library to manipulate the image we generated.




## DALL-E

In the previous lessons, we discussed how to generate images using DALL-E 2. Now, we will dive into the exciting world of image manipulation, enabling you to create a wide variety of variations from the original generated image.

|||
**DALL-E** 2 is a powerful AI model developed by OpenAI that can generate high-quality images from textual descriptions. However, the API is not limited to just generating images - it also allows you to manipulate the generated images by adjusting certain parameters. We will explore how to change image size, aspect ratio, brightness, contrast, saturation, hue, and other properties using the DALL-E 2 API.
 
|||

## Generating Image
Let's get started with a simple code example that demonstrates how to adjust some of these parameters. In this example, we will generate an image of a "red apple" and then manipulate its properties to create different variations.
In order to generate an image using the DALL·E we can use the `openai.Image.create` call. This time we are going to create a function that will take our prompt as an argument and manipulate it from there. We are going to import our libraries and API key then we are going to create our function. 
``` python
import os
import openai
import secret
from PIL import Image, ImageOps
from io import BytesIO
import requests

openai.api_key = secret.api_key

# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

base_image_url = generate_base_image('red apple')


```

In order to not have to keep copying and pasting our result in, we are going to save the image inside the URL as a file in our Codio box. 

```
img_data = requests.get(base_image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)
```
{Try it!}(python3 imageGen.py 2)
[Click here to refresh your image](close_file image_name.jpg panel=1; open_file image_name.jpg panel=1) 

After generating our image we are going to comment out the function for the code generation. Since our image is saved in a file we can just interact with that now. We can use multi-line comments using the following syntax `"""  """`.

{Check It!|assessment}(multiple-choice-2638589816)
