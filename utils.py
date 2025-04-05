import math
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


def draw_palette(
    palette_name: str,
    palette: str,
    number_of_cols: int = 5,
    radius: float = 0.15,
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
    # number_of_cols = number_of_cols
    if number_of_colors < number_of_cols:
        number_of_rows = 1
    else:
        number_of_rows = math.ceil(number_of_colors / number_of_cols)
    # number_of_subplots = number_of_cols * number_of_rows
    square_size = radius * 2.1
    spacing = 0.05


    fig_width = number_of_cols * (square_size + spacing)
    fig_height = number_of_rows * (square_size + spacing)

    
    fig = plt.figure(figsize=(fig_width, fig_height))

    for idx in range(number_of_cols * number_of_rows):
        row = idx // number_of_cols
        col = idx % number_of_cols

        if idx < number_of_colors:
            color = palette[idx]
        else:
            color = (1, 1, 1)

        left = col * (square_size + spacing) / fig_width
        bottom = 1 - (row + 1) * (square_size + spacing) / fig_height
        width = square_size / fig_width
        height = square_size / fig_height

        ax = fig.add_axes([left, bottom, width, height])
        ax.add_patch(Circle((0.5,0.5), radius / square_size, facecolor = color, edgecolor="#0f0f0f", linewidth = 1))

        ax.set_xlim(0, 1)
        ax.set_ylim(0,1)
        ax.set_aspect("equal")
        ax.axis("off")

        if idx == 0:
            ax.set_title(palette_name, loc="left", fontsize="x-small")



    # # Create figure and dynamically assign number of rows and columns
    # fig, ax = plt.subplots(
    #     number_of_rows,
    #     number_of_cols,
    #     figsize=(number_of_cols * square_size, number_of_rows * square_size),
    #     constrained_layout=True,
    # )
    # ax = ax.flatten()

    # # Iterate through the indivudal subplots and the palette. Draw a 
    # # circle at the center of the square and fill it with the palette's
    # # color of the current iteration.
    # for square_no in range(number_of_subplots):
    #     if square_no < number_of_colors:
    #         ax[square_no].add_patch(
    #             Circle((square_size/2, square_size/2), radius, color=palette[square_no])
    #         ) 
    #     else:
    #         ax[square_no].set_facecolor((1, 1, 1))

    #     if square_no == 0:
    #         ax[square_no].set_title(palette_name, loc="left", fontsize="x-small")

    #     ax[square_no].set_xlim(0, square_size)
    #     ax[square_no].set_ylim(0, square_size)
    #     ax[square_no].set_frame_on(False)
    #     ax[square_no].set_xticks([])
    #     ax[square_no].set_yticks([])
    #     ax[square_no].set_aspect("equal")

    return fig


if __name__ == "__main__":
    from pixelator import Pixelator

    pixelator = Pixelator()
    # palettes = pixelator.get_palettes("RGB")
    palettes = pixelator.get_palettes("")

    for palette_name, palette in palettes.items():
        fig = draw_palette(palette_name, palette, 5)
        plt.show()
        plt.close(fig)
        break

