import json
from PIL import ImageColor
from typing import Dict, List


class Palettes:
    """Class for handling color palettes.

    Attributes:
        default_palettes_file_path (str): the default path to the JSON
            file containing the color palettes hex codes (default:
            assets/palettes_hex.json)
    """

    def __init__(self, default_palettes_file_path: str = "assets/palettes_hex.json"):
        """Initialize the Palettes class with the default color palette 
        file path.

        Args:
            default_palettes_file_path (str): the default path to the 
            JSON file containing the color palettes hex codes (default:
            assets/palettes_hex.json)
        """
        self.default_palettes_file_path = default_palettes_file_path

    def create_rgb_palettes(
        self, palettes_file_path: str = None
    ) -> Dict[str, List[tuple]]:
        """Convert the palettes' hex color codes into RGB.

        Args:
            palettes_file_path (optional, str): file path to the 
                palettes JSON file.
        """
        palettes_file_path = palettes_file_path or self.default_palettes_file_path
        rgb_palettes = {}

        with open(palettes_file_path, "r") as file:
            palettes = json.load(file)

        for palette_name, palette in palettes.items():
            rgb_palettes[palette_name] = [
                ImageColor.getcolor(hex_code, "RGB") for hex_code in palette
            ]
        return rgb_palettes


if __name__ == "__main__":
    instance_test = Palettes()
    palette_test = instance_test.create_rgb_palettes()
    print(type(palette_test))
    print(palette_test)
