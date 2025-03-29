from io import BytesIO
import streamlit as st

from pixelator import Pixelator
from utils import load_palettes

pixelator = Pixelator()

st.title("Pixelator")
st.subheader("Create pixel art from any image!")

# Inputs
original_image = st.file_uploader("Upload", type=["jpg"])
pixel_size = st.select_slider("Select pixel size", options=[i for i in range(1, 11)])
palette = st.selectbox(
    # "Color palette", ["No palette", *load_palettes().keys()], index=None
    "Color palette", ["No palette", *pixelator.get_palettes("RGB").keys()], index=None
)
if palette == "No palette":
    palette = ""
else:
    palette = palette

# Pixelate
if original_image:
    with st.status("Pixelating..."):
        pixelated_image = pixelator.pixelate(original_image, pixel_size, palette)

    st.image(pixelated_image)

    # Save the pixelated image to a temporary binary stream and
    # retrieve it from there to download. Workaround to access files
    # from st.file_uploader.

    temp_buffer = BytesIO()
    pixelated_image.save(temp_buffer, format="JPEG")
    buffered_image = temp_buffer.getvalue()
    st.download_button(
        label="Download",
        data=buffered_image,
        file_name="pixelator.jpg",
        mime="image/jpeg",
    )
