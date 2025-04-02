import math
import matplotlib.pyplot as plt


def draw_palette(
    palette_name: str,
    palette: list[tuple],
    cols: int = 5,
    rect_width: float = 0.3,
    rect_height: float = 0.11,
) -> plt.Figure:
    """Generates and returns a matplotlib Figure displaying a color palette.

    This function creates a grid of colored rectangles based on the given palette,
    arranging them in a specified number of columns. Each color is displayed as
    a small rectangle, and any empty slots are filled with white rectangles.

    Args:
        palette_name (str): The name of the palette to be displayed.
        palette (list[tuple]): A list of RGB color tuples, where each tuple
            consists of three integers representing red, green, and blue
            values (0-255).
        cols (int, optional): The number of columns in the grid. Defaults to 5.
        rect_width (float, optional): The width of each rectangle in the grid. Defaults to 0.3.
        rect_height (float, optional): The height of each rectangle in the grid. Defaults to 0.11.

    Returns:
        plt.Figure: A matplotlib Figure object containing the plotted palette.
    """
    # Set plot parameters
    number_of_colors = len(palette)
    cols = cols
    rows = math.ceil(number_of_colors / cols)
    number_of_squares = cols * rows
    fig_width = cols * rect_width
    fig_height = rows * rect_height

    # Create figure and dynamically assign number of rows and columns
    fig, ax = plt.subplots(rows, cols, figsize=(fig_width, fig_height))
    ax = ax.flatten()

    # Iterate through the indivudal rectangles and the palette and color
    # the rectangles accordingly
    for rect_no in range(number_of_squares):
        if rect_no < number_of_colors:
            ax[rect_no].imshow([[palette[rect_no]]], norm=plt.Normalize(0, 255))
        else:
            ax[rect_no].imshow([[(255, 255, 255)]], norm=plt.Normalize(0, 255))

        if rect_no == 0:
            ax[rect_no].set_title(palette_name, loc="left", fontsize="x-small")

        ax[rect_no].set_frame_on(False)
        ax[rect_no].set_xticks([])
        ax[rect_no].set_yticks([])
        ax[rect_no].set_aspect(rect_height / rect_width)

    return fig


if __name__ == "__main__":
    from pixelator import Pixelator
    
    pixelator = Pixelator()
    palettes = pixelator.get_palettes("RGB")

    for palette_name, palette in palettes.items():
        fig = draw_palette(palette_name, palette)
        plt.show()
        plt.close(fig)
        break
