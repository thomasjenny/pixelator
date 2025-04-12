import json
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from PIL import Image, ImageColor


class Pixelator:
    """A class to create pixelated versions of images using various
    color palettes.

    Attributes:
        palettes_file_path (str, optional): path to the color palattes
            JSON file used for recoloring the image.
    """

    def __init__(self, palettes_file_path: str = "assets/palettes_hex.json"):
        """Initializes a Pixelator instance with a path to the palettes
        JSON file.

        Args:
            palettes_file_path (str, optional): path to the JSON file
                containing the color palettes. Defaults to
                "assets/palettes_hex.json".
        """
        self.palettes_file_path = palettes_file_path
        self.pixelated_image = None

    def get_palettes(self, mode: str = "rgb") -> dict[str, list[tuple]]:
        """Loads color palettes from a JSON file and converts them from
        HEX to RGB.

        Args:
            mode(str, optional): color mode for palettes. If set to
            "RGB", the palette's hex codes are converted to RGB tuples,
            otherwise, the original HEX codes are returned.

        Returns:
            dict[str, list[tuple]]: dict with palette names as keys
                and color values as values (either RGB tuples or HEX
                strings).
        """
        palettes = {}
        palettes_file_path = self.palettes_file_path

        with open(palettes_file_path, "r") as file:
            palettes_raw = json.load(file)

        if mode.lower() == "hex":
            palettes = palettes_raw
        elif mode.lower() == "rgb":
            for palette_name, palette in palettes_raw.items():
                palettes[palette_name] = [
                    ImageColor.getcolor(hex_code, "RGB") for hex_code in palette
                ]
        else:
            palettes = palettes_raw

        return palettes

    def recolor_pixel(self, square: np.ndarray, palette: str = "") -> list[int]:
        """Calculates the average RGB color of a pixel square and
        recolors it.

        This function computes the average color of all pixels in a
        square region and optionally replaces it with the closest
        matching color from a given color palette.

        Args:
            square (np.ndarray): 2D numpy array where each element is
                a pixel represented as an array of red, green, and blue
                values.
            palette (str, optional): name of the color palette to use
                for recoloring the pixel square. If not specified, the
                average color of all pixels in the square used
                (default).

        Returns:
            list[int]: list of three integers representing the new RGB
                color.
        """
        # Prepare arrays for average color calculation
        square_height = len(square)
        square_width = len(square[0])
        no_of_pixels_in_square = square_height * square_width

        reds = np.zeros(no_of_pixels_in_square, dtype=np.int64)
        greens = np.zeros(no_of_pixels_in_square, dtype=np.int64)
        blues = np.zeros(no_of_pixels_in_square, dtype=np.int64)

        # Store each r, g, b value in the square
        index = 0
        for row in square:
            for pixel in row:
                reds[index] = pixel[0]
                greens[index] = pixel[1]
                blues[index] = pixel[2]
                index += 1

        # Calculate average color
        red_avg = int(np.sum(reds) / no_of_pixels_in_square)
        green_avg = int(np.sum(greens) / no_of_pixels_in_square)
        blue_avg = int(np.sum(blues) / no_of_pixels_in_square)
        rgb_avg = [red_avg, green_avg, blue_avg]

        # Get color palettes
        palettes = self.get_palettes("RGB")
        # Calculate the index of the closest color in the palette
        if palette in palettes.keys():
            palette = palettes[palette]
            closest_color_index = np.linalg.norm(
                np.array(rgb_avg) - np.array(palette), axis=1
            ).argmin()
            rgb_new = list(palette[closest_color_index])
        else:
            rgb_new = rgb_avg

        return rgb_new

    def pixelate(
        self, image_path: str, pixel_size: int, palette: str = ""
    ) -> Image.Image:
        """Pixelates an image and optionally recolors it using a
        specified palette.

        This funciton loads an image, processes it by dividing it into
        square regions of the specified pixel size, and recolors each
        region based on the chosen palette.

        Args:
            image_path (str): path to the image to be pixelated.
            pixel_size (int): size of the pixel blocks in the pixelated
                image.
            palette (str, optional): name of the color palette to apply.
                If not specified, the average color of each pixel block
                is used (default).

        Returns:
            Image.Image: the pixelated image.
        """
        print(f"Pixelating {image_path}...")

        # Convert image to numpy array
        with Image.open(image_path) as im:
            image_array = np.asarray(im)

        # Create an empty numpy array for the pixelated image. If
        # needed, cut off pixels so that image height and width fits
        # pixel size n times without remainder.
        original_image_height, original_image_width, _ = image_array.shape
        new_image_height = original_image_height - (original_image_height % pixel_size)
        new_image_width = original_image_width - (original_image_width % pixel_size)
        new_image = np.zeros((new_image_height, new_image_width, 3), dtype=np.uint8)

        # Iterate over the image in squares determined by pixel_size
        for i in range(0, new_image_height, pixel_size):
            for j in range(0, new_image_width, pixel_size):
                # Extract a square and recolor
                square = image_array[i : i + pixel_size, j : j + pixel_size]
                RGB_new = self.recolor_pixel(square, palette)
                # Add recolored square to the new image's numpy array
                new_image[i : i + pixel_size, j : j + pixel_size] = RGB_new

        self.pixelated_image = Image.fromarray(new_image)

        return self.pixelated_image

    def show_image(self):
        """Displays the pixelated image (if created)."""
        if self.pixelated_image is not None:
            plt.imshow(self.pixelated_image)
            plt.axis("off")
            plt.show()
        else:
            print(
                "No pixelated image has been generated yet. "
                "Call 'pixelate()' first to generate a pixelated image."
            )

        return None

    def save_image(self, out_path: str, out_img_name: str):
        """Saves the pixelated image to the specified file path (if 
        created).

        Args:
            out_path (str): ath where the pixelated image should be
                saved.
            out_img_name (str): name of the image to be saved.
        """
        if self.pixelated_image is not None:
            img_out_path = Path(Path.cwd() / out_path)
            os.makedirs(img_out_path, exist_ok=True)
            self.pixelated_image.save(Path(img_out_path / out_img_name))
        else:
            print(
                "Image cannot be saved - no pixelated image has been generated yet. "
                "Call 'pixelate()' first to generate a pixelated image."
            )

        return None


if __name__ == "__main__":
    pixelator = Pixelator()

    in_path = "examples/01_original.jpg"
    out_path = "examples"
    out_name = "01_test.jpg"

    # Test the show and save functions before pixelating (they won't work)
    pixelator.show_image()
    pixelator.save_image(out_path, out_name)

    # Pixelate image, show it and save it
    pixelator.pixelate(in_path, 3, "shimmering_sunset")
    pixelator.show_image()
    pixelator.save_image(out_path, out_name)
