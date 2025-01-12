import pandas as pd
from pixelator import Pixelator
import streamlit as st
from utils import generate_color_dfs, style_color_df


st.title("Test")

img = st.file_uploader("Upload", type=["jpg"])

# Display the image (only if an image has been selected)
if img is not None:
    st.image(img)

# Generate a dictionary that contains the palette name (key) and a 5-column
# wide dataframe with all hex values (value)
palettes = generate_color_dfs()
# Select one of the palettes (= dataframe)
pico8 = palettes["pico-8"]

# Create the style dataframe (returns a copy of the original df, but each cell
# contains f"background-color: {cell hex value}")
style_df = style_color_df(pico8)

# Apply the styling to the original df (color each cell)
styled_df = pico8.style.apply(lambda x: style_df, axis=None)

# Display the styled dataframe in Streamlit
st.dataframe(styled_df)
