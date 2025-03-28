import json
import numpy as np
from PIL import Image, ImageColor


class Pixelator:
    """A class to create pixelated versions of images using various
    color palettes.

    Attributes:
        palettes_file_path (str, optional): path to the color palattes
            file used to recolor the image.
    """

    def __init__(self, palettes_file_path: str = "assets/palettes_hex.json"):
        self.palettes_file_path = palettes_file_path

    def get_palettes(self, mode: str = "RGB") -> dict[str, list[tuple]]:
        """Load all palettes with their hex color codes, convert them
        to RGB, and return the RGB palettes. Uses the default file path
        as defined on class level.
        """
        palettes = {}
        palettes_file_path = self.palettes_file_path

        with open(palettes_file_path, "r") as file:
            palettes_raw = json.load(file)

        if mode == "RGB":
            for palette_name, palette in palettes_raw.items():
                palettes[palette_name] = [
                    ImageColor.getcolor(hex_code, "RGB") for hex_code in palette
                ]
        elif mode == "HEX":
            palettes = palettes_raw

        return palettes

    def recolor_pixel(self, square: np.ndarray, palette: str = "") -> list[int]:
        """Calculates the average red, green, and blue values of all
        pixels in a given square with the following size: square side
        length * square side length.

        Args:
            square (np.ndarray): 2D numpy array where each element is
                a pixel represented as an array of red, green, and blue
                values.
            palette (str, optional): name of the color palette to
                recolor the pixel. If not specified, the average color
                of all pixels in the square used (default).

        Returns:
            list[int]: list of three integers representing the new red,
                green, and blue values.
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
        """Pixelates and recolors the image.

        Args:
            image_path (str): path to the image to be pixelated.
            pixel_size (int): size of the pixels in the pixelated image
            palette (str, optional): name of the color palette to
                recolor the pixel. If not specified, the average color
                of all pixels in the square used (default).

        Returns:
            Image.Image: the pixelated image.
        """
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

        new_img = Image.fromarray(new_image)

        return new_img


if __name__ == "__main__":
    image_path = "img/wave.jpg"
    pixelator = Pixelator()
    test = pixelator.pixelate(image_path, 3, "shimmering_sunset")
    test.show()
