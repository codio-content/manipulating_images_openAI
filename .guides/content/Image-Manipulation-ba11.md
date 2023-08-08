### Image Manipulation Function
---
We first generated a base image of a "red apple" using the DALL-E 2 API. We saved our image as `image_name.jpg`. I know really creative. Now, we are going to access that image and start manipulating it. The first step we are going to do is to create a variable that points to our first image and calls that `base_image`.


```python
"""
base_image_url = generate_base_image('red apple')
"""
base_image = Image.open('image_name.jpg')
```

{Try it!}(python3 imageGen.py 3)
[Click here to refresh your base image](close_file image_name.jpg panel=1; open_file image_name.jpg panel=1) 

Now we are ready to create a function that will interact with the `PIL` library. The function takes a couple of variables as arguments. Let's start by defining what those are. 
```python-hide-clipboard
def manipulate_image(image, size, aspect_ratio, brightness, contrast, saturation, hue)
```
|||
1. **image**: A PIL image object representing the base image that you want to manipulate.
1. **size**: A float value between 0 and 1, representing the scale factor by which you want to resize the image. A value of 1 will keep the original size, while a value of 0.5 will reduce the size by half, and a value of 0.75 will resize the image to 75% of its original size.
1. **aspect_ratio**: A float value representing the aspect ratio for resizing the image. A value of 1 will maintain the original aspect ratio, while values greater than 1 will stretch the image vertically and values less than 1 will stretch the image horizontally.
1. **brightness**: A float value representing the factor by which to adjust the image's brightness. A value of 1 means no change, while values greater than 1 will increase brightness, and values less than 1 will decrease brightness.
1. **contrast**: A float value representing the factor by which to adjust the image's contrast. A value of 1 means no change, while values greater than 1 will increase contrast, and values less than 1 will decrease contrast.
1. **saturation**: A float value representing the factor by which to adjust the image's color saturation. A value of 1 means no change, while values greater than 1 will increase saturation, and values less than 1 will decrease saturation.
1. **hue**: A float value representing the amount by which to adjust the image's hue. A value of 0 means no change, while positive and negative values will rotate the hue in different directions.

|||


```python
# Manipulate the image properties
def manipulate_image(image, size, aspect_ratio, brightness, contrast, saturation, hue):
    # Resize the image
    new_size = (int(image.width * size), int(image.height * aspect_ratio * size))
    resized_image = image.resize(new_size, Image.ANTIALIAS)

    # Adjust the image properties
    from PIL import ImageEnhance, ImageOps
    enhanced_image = ImageEnhance.Brightness(resized_image).enhance(brightness)
    enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(contrast)
    enhanced_image = ImageEnhance.Color(enhanced_image).enhance(saturation)
    
    # Adjust hue using ImageOps module
    enhanced_image = ImageOps.colorize(enhanced_image.convert('L'), 'black', 'white', midpoint=128 - int(128 * hue))

    return enhanced_image
```
The following Try It button is to make sure everything runs without errors.
{Try it!}(python3 imageGen.py 4)
We define a function `manipulate_image()` that takes in the base image and various parameters for image manipulation. We use the Python Imaging Library (PIL) to resize the image, and adjust its brightness, contrast, saturation, and hue. We use `ImageOps.colorize()` to adjust the hue of the image.

```python
 # Example of image manipulation
manipulated_image = manipulate_image(
  base_image, size=0.5, aspect_ratio=1, brightness=1.2,
  contrast=1.5, saturation=0.8, hue=0.1
)
```
{Try it!}(python3 imageGen.py 5)
Finally, we demonstrate how to use this function to create a manipulated version of the original image by adjusting the parameters.


Now we are going to save our manipulated image as `manipulated_red_apple.jpg`.
```
# Save the manipulated image to a file
manipulated_image.save('manipulated_red_apple.jpg')
```
{Try it!}(python3 imageGen.py 51)

[Click here to open manipulated_red_apple.jpg](close_file manipulated_red_apple.jpg panel=1; open_file manipulated_red_apple.jpg panel=1)

---


{Check It!|assessment}(multiple-choice-338336817)
