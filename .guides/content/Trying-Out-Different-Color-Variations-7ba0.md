### Keep color
Let's try creating an extra variation. This time we are going to keep the color the same. Try out variations. 

To maintain the original color when the hue is 0, we can do the following that will run when the hue is not 0. Add the code below into the `manipulate_image()` function .
```python
# Adjust hue only if hue is not 0
if hue != 0:
    # Convert image to HSV
    hsv_image = enhanced_image.convert('HSV')
    # Shift hue value
    hsv_image = hsv_image.point(lambda p: (p + int(256 * hue)) % 256 if p < 256 else p)
    # Convert back to RGB
    enhanced_image = hsv_image.convert('RGB')
```

The `ImageOps.colorize()` function used in the code is converting the image to grayscale. We first check if the hue parameter is not 0 before adjusting the hue of the image. If the hue is 0, the color of the image remains unchanged.

In the following example, we've changed the size parameter to 0.8 (80% of the original size) and kept the aspect ratio at 1 to maintain the original aspect ratio. The brightness, contrast, saturation, and hue parameters are set to their default values to keep the color properties unchanged. Let's try the following example,

```python
# Example of image manipulation with only size change
size_changed_image = manipulate_image(
    base_image, size=0.8, aspect_ratio=1, brightness=1,
    contrast=1, saturation=1, hue=0
)

# Save the size-changed image to a file
size_changed_image.save('size_changed_red_apple.jpg')
```
{Try it!}(python3 imageGen.py 32)
[Click here to refresh your sized image](close_file size_changed_red_apple.jpg panel=1; open_file size_changed_red_apple.jpg panel=1) 
The resulting image will be saved as `size_changed_red_apple.jpg` in the same folder as your script.

# Purple
Now let's try making it more purple. 
```python
# Example of image manipulation with a more purple hue
purple_image = manipulate_image(
    base_image, size=1, aspect_ratio=1, brightness=1,
    contrast=1, saturation=1, hue=0.8
)

# Save the purple image to a file
purple_image.save('purple_red_apple.jpg')
```
{Try it!}(python3 imageGen.py 30)
[Click here to refresh your purple image](close_file purple_red_apple.jpg panel=1; open_file purple_red_apple.jpg panel=1)


In this example, we set the hue parameter to 0.8, which shifts the hue towards the purple range. The size, aspect ratio, brightness, contrast, and saturation parameters are set to their default values to maintain the original properties of the image.

The resulting image will be saved as `purple_red_apple.jpg` in the same folder as your script. Please note that the hue value of 0.8 is just an example, and you may need to adjust the value to achieve the desired shade of purple.

Try the purple image with a different combination of saturation. For example, try it with the following : `0`, `0.5` , `2` .

{Try it!}(python3 imageGen.py 5)
[Click here to refresh your purple image](close_file purple_red_apple.jpg panel=1; open_file purple_red_apple.jpg panel=1)

We have demonstrated how to create variations of an image using the `manipulate_image()` function. You can use this function to create different versions of an image with varying size, aspect ratio, brightness, contrast, saturation, and hue.

To create a version of the image with the original color, set the hue parameter to 0. In the provided code, we first check if the hue parameter is not 0 before adjusting the hue of the image. If the hue is 0, the color of the image remains unchanged.

We have also provided examples of how to create a resized version of the image, as well as a version with a more purple hue. You can experiment with different combinations of parameters to achieve the desired look for your image.

{Check It!|assessment}(multiple-choice-3470323804)
