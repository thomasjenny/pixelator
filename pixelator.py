import json
# import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image, ImageColor
from typing import Dict, List


class Pixelator:
    """Pixelator class

    Attributes:
    """

    # def __init__(self, palettes: Dict[str, List[tuple]], img_path: str) -> None:
    def __init__(self, palettes_file_path: str = "assets/palettes_hex.json"):
        """Initialize the Pixelator class

        Args:
            x
        """
        # self.img_path = img_path
        self.palettes_file_path = palettes_file_path

    def get_palettes(self) -> Dict[str, List[tuple]]:
        """Load all palettes with their hex color codes and convert them
        to RGB.

        Args:
            x
        """
        rgb_palettes = {}
        palettes_file_path = self.palettes_file_path

        with open(palettes_file_path, "r") as file:
            palettes = json.load(file)

        for palette_name, palette in palettes.items():
            rgb_palettes[palette_name] = [
                ImageColor.getcolor(hex_code, "RGB") for hex_code in palette
            ]

        return rgb_palettes

    def recolor_pixel(self, square: np.array, palette: str = ""):  # , palette: str) -> List:
        """Calculates the average red, green, and blue values of all
        pixels in a given square with size (square side length x square
        side length).
        """
        # Store each r, g, b value for the square
        reds, blues, greens = [], [], []
        for row in square:
            for pixel in row:
                reds.append(pixel[0])
                greens.append(pixel[1])
                blues.append(pixel[2])

        # Calculate the average r, g, b values

        ########################################
        ########################################
        ########################################

        # HANDLE OVERFLOW WARNING HERE!

        red_avg = int(sum(reds) / len(reds))
        green_avg = int(sum(greens) / len(greens))
        blue_avg = int(sum(blues) / len(blues))
        RGB_avg = [red_avg, green_avg, blue_avg]
        # print(RGB_avg)

        ########################################
        ########################################
        ########################################

        # Get the color palettes
        palettes = self.get_palettes()

        if palette in palettes.keys():
            palette = palettes[palette]
            color_index = np.linalg.norm(
                np.array(RGB_avg) - np.array(palette), axis=1
            ).argmin()
            RGB_new = list(palette[color_index])
        else:
            RGB_new = RGB_avg

        return RGB_new

    def pixelate(self, image_path, pixel_size, palette = ""):
        # Open the image and convert it to a np array
        with Image.open(image_path) as im:
            image_array = np.asarray(im)
            # print(image_array)

        # Create a numpy array for the pixelated image whose height and
        # width are divisible by the output pixel size without remainder
        original_image_height, original_image_width, _ = image_array.shape
        new_image_height = original_image_height - (original_image_height % pixel_size)
        new_image_width = original_image_width - (original_image_width % pixel_size)
        new_image = np.zeros((new_image_height, new_image_width, 3), dtype=np.uint8)

        # Iterate over the image in squares determined by pixel_size
        for i in range(0, new_image_height, pixel_size):
            for j in range(0, new_image_width, pixel_size):
                # Extract a square
                square = image_array[i:i + pixel_size, j:j + pixel_size]
                # Calculate the new color for the square
                RGB_new = self.recolor_pixel(square, palette)
                # Add a square in the color of RGB_new to the np array
                # for the new image
                new_image[i:i + pixel_size, j:j + pixel_size] = RGB_new

        # Convert the new image array to an image
        new_img = Image.fromarray(new_image)

        return new_img


if __name__ == "__main__":
    # print(Pixelator.__doc__)

    pixelator = Pixelator()

    # pixelator.pixelate("img/lamborghini_small.jpg", 5)

    # palettes = pixelator.get_palettes()
    # print(palettes)

    image_path = "img/lamborghini_small.jpg"
    # with Image.open(image_path) as im:
    #    image_array = np.asarray(im)
    
    no_pal = pixelator.pixelate(image_path, 5, "pico-8")
    # no_pal.show()

    # original_image_height, original_image_width, _ = image_array.shape
# 
    # new_image_height = original_image_height - (original_image_height % 5)
    # new_image_width = original_image_width - (original_image_width % 5)
    # new_image = np.zeros((new_image_height, new_image_width, 3), dtype=np.uint8)
# 
    # for i in range(0, new_image_height, 5):
    #     for j in range(0, new_image_width, 5):
    #         # Extract a square
    #         square = image_array[i : i + 5, j : j + 5]
    #         break
    # 
    # print(square)
    # RGB_new = pixelator.recolor_pixel(square)#, "shimmering_sunset")
    # print(RGB_new)
