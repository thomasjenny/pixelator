import math
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


def draw_palette(
    palette_name: str,
    palette: list[str],
    number_of_cols: int = 5,
    radius: float = 0.15,
    plot_palette_name: bool = False,
) -> plt.Figure:
    """Generates and returns a matplotlib Figure displaying a color
    palette.

    This function creates a grid of colored circles based on the given
    palette, arranging them in a specified number of columns. Each color
    is displayed as a circle.

    Args:
        palette_name (str): The name of the palette to be displayed.
        palette (list[str]): A list of hexadecimal color tuples.
        number_of_cols (int, optional): The number of columns in the
            grid. Defaults to 5.
        raduis (float, optional): The radius of each circle in the grid.
            Defaults to 0.15.
        plot_palette_name (bool, optional): If set to True, the palette
            name is plotted in the top-left corner above the palette
            grid. Defaults to False.

    Returns:
        plt.Figure: A matplotlib Figure object containing the plotted palette.
    """
    # Set plot parameters
    number_of_colors = len(palette)
    # Length/width of each ax in the grid. Circles are plotted on the
    # axes.
    ax_size = radius * 2.1
    # Spacing between the axes
    spacing = 0.05
    # Number of rows depending on number of colors and columns
    if number_of_colors < number_of_cols:
        number_of_rows = 1
    else:
        number_of_rows = math.ceil(number_of_colors / number_of_cols)
    # Total size of the plot
    fig_width = number_of_cols * (ax_size + spacing)
    fig_height = number_of_rows * (ax_size + spacing)

    # Create plot with transparent background
    fig = plt.figure(figsize=(fig_width, fig_height))
    fig.set_facecolor("none")

    for i in range(number_of_cols * number_of_rows):
        # Get position of current ax on the grid
        row = i // number_of_cols
        col = i % number_of_cols

        # Assign color from palette or transparency if axes are only
        # used to fill the grid
        if i < number_of_colors:
            color = palette[i]
        else:
            color = "none"

        # Calculate parameters for plotting the ax
        left = col * (ax_size + spacing) / fig_width
        bottom = 1 - (row + 1) * (ax_size + spacing) / fig_height
        width = ax_size / fig_width
        height = ax_size / fig_height

        # Add the circle if the current position is in the color range
        ax = fig.add_axes([left, bottom, width, height])
        if i < number_of_colors:
            ax.add_patch(
                Circle(
                    (0.5, 0.5),
                    radius / ax_size,
                    facecolor=color,
                    edgecolor="#0f0f0f",
                    linewidth=0.5,
                )
            )

        # Style the plot
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect("equal")
        ax.axis("off")

        # Plot palette name
        if plot_palette_name == True:
            if i == 0:
                ax.set_title(palette_name, loc="left", fontsize="x-small")

    return fig


if __name__ == "__main__":
    from pixelator import Pixelator

    pixelator = Pixelator()
    palettes = pixelator.get_palettes("HEX")

    for palette_name, palette in palettes.items():
        fig = draw_palette(palette_name, palette, 5)
        plt.show()
        plt.close(fig)
        break
