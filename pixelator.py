import json
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
from typing import Dict, List

from palettes import Palettes


class Pixelator:
    """Pixelator class
    
    Attributes:
    """

    # def __init__(self, palettes: Dict[str, List[tuple]], img_path: str) -> None:
    def __init__(self):
        """Initialize the Pixelator class 

            Args:
                palettes (Dict): dict containing the color palettes
                img_path (str): path to the image that should be 
                    pixelated
            """
        # self.palettes = palettes
        # self.img_path = img_path
        self.palettes = Palettes.create_rgb_palettes()

    def calculate_square_color(square: np.array, palette: str) -> List:
        """Calculates the average red, green, and blue values of all 
        pixels in a given square with size (square side length x square 
        side length).
    
        Args:
            square (np.array) : array of shape (square side length, 
                square side length, 3)
            palette (str) : color palette used to recolor the pixelated
                image. If not specified, the average color of all pixels
                in the square is used.
    
        Returns:
            RGB_new (List) : list of length 3 that contains the new red,
                green, and blue values. The RGB values are either the 
                average of all pixels in the square or the nearest RGB
                value from the chosen palette (i.e., the value with
                the smallest euclidean distance to the square's average).
        """
        # Store each r, g, b value for the square
        reds, blues, greens = [], [], []
        for row in square:
            for pixel in row:
                reds.append(pixel[0])
                greens.append(pixel[1])
                blues.append(pixel[2])

        # Calculate the average r, g, b values
        red_avg = int(sum(reds) / len(reds))
        green_avg = int(sum(greens) / len(greens))
        blue_avg = int(sum(blues) / len(blues))
        RGB_avg = [red_avg, green_avg, blue_avg]

    def test_palettes(self):
        testpal = Palettes.create_rgb_palettes()
        print(testpal)
        return testpal
        


if __name__ == "__main__":
    # print(Pixelator.__doc__)

    pixelator = Pixelator()

    print("Load Palettes:", pixelator.palettes)

    test_palette = pixelator.test_palettes()
    print("Test Palettes:", test_palette)


