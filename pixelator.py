import json
import matplotlib.pyplot as plt
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

    # def calculate_square_color(square: np.array, palette: str) -> List:
    #     """Calculates the average red, green, and blue values of all
    #     pixels in a given square with size (square side length x square
    #     side length).

    #     Args:
    #         square (np.array) : array of shape (square side length,
    #             square side length, 3)
    #         palette (str) : color palette used to recolor the pixelated
    #             image. If not specified, the average color of all pixels
    #             in the square is used.

    #     Returns:
    #         RGB_new (List) : list of length 3 that contains the new red,
    #             green, and blue values. The RGB values are either the
    #             average of all pixels in the square or the nearest RGB
    #             value from the chosen palette (i.e., the value with
    #             the smallest euclidean distance to the square's average).
    #     """
    #     # Store each r, g, b value for the square
    #     reds, blues, greens = [], [], []
    #     for row in square:
    #         for pixel in row:
    #             reds.append(pixel[0])
    #             greens.append(pixel[1])
    #             blues.append(pixel[2])
    #
    #     # Calculate the average r, g, b values
    #     red_avg = int(sum(reds) / len(reds))
    #     green_avg = int(sum(greens) / len(greens))
    #     blue_avg = int(sum(blues) / len(blues))
    #     RGB_avg = [red_avg, green_avg, blue_avg]

    def pixelate(self, image_path, pixel_size, palette):
        # Open the image and convert it to a np array
        with Image.open(image_path) as im:
            image_array = np.asarray(im)
            print(image_array)

        # Create a numpy array for the pixelated image whose height and
        # width are divisible by the output pixel size without remainder
        original_image_height, original_image_width, _ = image_array.shape
        new_image_height = original_image_height - (original_image_height % pixel_size)
        new_image_width = original_image_width - (original_image_width % pixel_size)
        new_image = np.zeros((new_image_height, new_image_width, 3), dtype=np.uint8)

        palettes = self.get_palettes()



if __name__ == "__main__":
    # print(Pixelator.__doc__)

    pixelator = Pixelator()

    pixelator.pixelate("img/lamborghini_small.jpg", 5)

    # palettes = pixelator.get_palettes()
    # print(palettes)
