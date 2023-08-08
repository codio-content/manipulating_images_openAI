----
The **hue** parameter in the `manipulate_image()` function is used to shift the hue values of the image, resulting in different color schemes. The hue value is a float, typically ranging from -1 to 1, where 0 means no change, positive values shift the hue clockwise in the color wheel, and negative values shift the hue counterclockwise.

Hue values in color space are typically represented in a circular form, often called a "color wheel." The color wheel is divided into 360 degrees, with different colors associated with different angle values:
|||
**Red**: 0 degrees (or 360 degrees)
**Yellow**: 60 degrees
**Green**: 120 degrees
**Cyan**: 180 degrees
**Blue**: 240 degrees
**Magenta**: 300 degrees

<p><a href="https://commons.wikimedia.org/wiki/File:HueScale.svg#/media/File:HueScale.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/HueScale.svg/1200px-HueScale.svg.png" alt="HueScale.svg"></a><br> <a href="https://commons.wikimedia.org/w/index.php?curid=1609109">Link</a></p>

|||

In the `manipulate_image()` function, we scale the hue parameter from -1 to 1 to cover the entire range of hue values. When the hue parameter is set to a specific value, the hue values in the image are shifted by that fraction of the full hue range (360 degrees).

For example:

- A hue value of 0.5 would shift the hue values by 180 degrees clockwise in the color wheel, effectively changing red to cyan, green to magenta, and blue to yellow.
- A hue value of -0.5 would shift the hue values by 180 degrees counterclockwise in the color wheel, effectively changing red to cyan, green to magenta, and blue to yellow (same as the previous example, since the shift is by 180 degrees).
- A hue value of 0.33 would shift the hue values by 120 degrees clockwise in the color wheel, effectively changing red to green, green to blue, and blue to red.
- A hue value of -0.25 would shift the hue values by 90 degrees counterclockwise in the color wheel, effectively changing red to yellow, green to cyan, and blue to magenta.


You can experiment with different hue values to achieve various color schemes for your image. Keep in mind that the color shifts might be more complex in real images, as they contain a mix of colors and may not always result in the exact colors mentioned in the examples.

----
### Saturation

**Saturation** is a color property that represents the intensity or purity of a color. It describes how vivid or dull a color appears. In the context of image processing, adjusting the saturation of an image can make the colors in the image appear more vibrant or more muted.

In the HSV (Hue, Saturation, and Value) color model, saturation is represented as a percentage (0% to 100%) or a value ranging from 0 to 1:

0% saturation (or a value of 0) means no color, resulting in a grayscale image.
100% saturation (or a value of 1) means the colors are fully saturated, appearing in their most intense form.

In our function, the saturation parameter is a float value that determines the factor by which the saturation of the image is adjusted:

- A saturation value of 1 means no change to the saturation of the image.
- Saturation values greater than 1 will increase the saturation of the image, making the colors appear more vivid and intense.
- Saturation values less than 1 and greater than 0 will decrease the saturation of the image, making the colors appear more muted or washed out.
- A saturation value of 2 would double the saturation of the colors in the image, making them appear more vibrant.
- A saturation value of 0.5 would reduce the saturation of the colors by half, making them appear more muted.
- A saturation value of 0 would remove all color from the image, resulting in a grayscale image.


When manipulating images, adjusting the saturation can have a significant impact on the overall appearance and mood of the image. Experimenting with different saturation values can help you achieve the desired look for your image.


{Check It!|assessment}(multiple-choice-1842835991)
