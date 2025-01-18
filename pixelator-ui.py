from io import BytesIO
import pandas as pd
from pixelator import Pixelator
import streamlit as st
from utils import load_palettes, generate_color_dfs, create_styling_df

from PIL import Image

st.title("Pixelator")
st.subheader("Create pixel art from any image!")


img = st.file_uploader("Upload", type=["jpg"])
# if img:
#     image = Image.open(img)
#     st.image(image)

pixel_size = st.select_slider(
    "Select pixel size",
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
)
# st.write(pixel_size)
# st.write(type(pixel_size))

palette = st.selectbox(
    "Color palette", ["No palette", *load_palettes().keys()], index=None
)

if palette == "No palette":
    palette = ""
else:
    palette = palette

if img:
    pixelator = Pixelator()
    pixelated_image = pixelator.pixelate(img, pixel_size, palette)
    # Save pixelated image in buffer
    # https://discuss.streamlit.io/t/how-to-download-image/3358/10
    buf = BytesIO()
    pixelated_image.save(buf, format="JPEG")
    byte_im = buf.getvalue()

preview_button = st.button("Preview", type="primary")
preview_button

if pixelated_image and preview_button:
    st.image(pixelated_image)

st.download_button(label="Save", data=byte_im, file_name="pixelator.jpg", mime="image/jpeg")

# Display the following only if an image has been selected:
# if img:
#     pixelator = Pixelator()
#     test = pixelator.pixelate(img, pixel_size, palette)
#     st.image(test)

# ----------------------------------------------------------------------
# # Generate a dictionary that contains the palette name (key) and a 5-column
# # wide dataframe with all hex values (value)
# palettes = generate_color_dfs()
# # Select one of the palettes (= dataframe)
# pico8 = palettes["pico-8"]

# # Create the style dataframe (returns a copy of the original df, but each cell
# # contains f"background-color: {cell hex value}")
# style_df = create_styling_df(pico8)

# # Apply the styling to the original df (color each cell)
# styled_df = pico8.style.apply(lambda x: style_df, axis=None)

# # Display the styled dataframe in Streamlit
# st.dataframe(styled_df)
# ----------------------------------------------------------------------


with st.expander("See color palettes"):
    st.header("Color palettes preview")

    # Generate a dictionary that contains the palette name (key) and a 5-column
    # wide dataframe with all hex values (value)
    palettes = generate_color_dfs()

    for palette_name, palette in palettes.items():
        style_df = create_styling_df(palette)
        styled_palette_df = palette.style.apply(lambda x: style_df, axis=None)
        st.write(palette_name)
        st.dataframe(styled_palette_df)


def palette_page():
    st.title("Color palette overview")

    for palette_name, palette in palettes.items():
        style_df = create_styling_df(palette)
        styled_palette_df = palette.style.apply(lambda x: style_df, axis=None)
        st.write(palette_name)
        st.dataframe(styled_palette_df)

pg = st.navigation([
    st.Page("pixelator-ui.py", title = "main", default=True),
    st.Page(palette_page, title = "test2"),
])

pg.run()