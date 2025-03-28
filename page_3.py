import math
import matplotlib.pyplot as plt
from PIL import ImageColor
import streamlit as st

from pixelator import Pixelator
from utils import load_palettes


pixelator = Pixelator()
palettes = pixelator.get_palettes("RGB")



def draw_palettes(palettes: dict[str, list[tuple]], cols: int, rect_width: float = 0.4, rect_height = 0.2) -> None:
    for pal in palettes:
        number_of_colors = len(palettes[pal])
        cols = cols
        rows = math.ceil(number_of_colors / cols)
        number_of_squares = cols * rows

        fig_width = cols * rect_width
        fig_height = rows * rect_height
        fig, ax = plt.subplots(rows, cols, figsize = (fig_width, fig_height))
        ax = ax.flatten()

        for rect in range(number_of_squares):
            if rect < number_of_colors:
                ax[rect].imshow([[palettes[pal][rect]]], norm = plt.Normalize(0, 255))
            else:
                ax[rect].imshow([[(255, 255, 255)]], norm = plt.Normalize(0, 255))
                ax[rect].set_frame_on(False)

            if rect == 0:
                ax[rect].set_title(pal, loc = "left", fontsize = "x-small")

            ax[rect].set_xticks([])
            ax[rect].set_yticks([])
            ax[rect].set_aspect(rect_height / rect_width)
        
        st.pyplot(fig, use_container_width=False)

    return None

draw_palettes(palettes, 5)


if __name__ == '__main__':
    draw_palettes(palettes, 5)