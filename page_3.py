import matplotlib.pyplot as plt
from PIL import ImageColor
import streamlit as st

# from pixelator import Pixelator
from utils import load_palettes


palettes = load_palettes()
print(palettes)
print(type(palettes))

def convert_hex_to_rgb(palette):
    return [ImageColor.getcolor(hex_color, "RGB") for hex_color in palette]


def display_palette(palette_name, colors):
    rgb_colors = [convert_hex_to_rgb(colors)]
    fig, ax = plt.subplots(figsize = (5, 1))
    ax.imshow(rgb_colors, aspect = "auto")
    st.pyplot(fig)

for name, colors in palettes.items():
    display_palette(name, colors)