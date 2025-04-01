from io import BytesIO
import math
import streamlit as st

from pixelator import Pixelator
from utils import draw_palette


st.set_page_config(layout="wide")


pixelator = Pixelator()


st.title("Pixelator")
st.subheader("Create pixel art from any image!")



col1, col2 = st.columns([2, 3], gap="large")

with col1:
    # Inputs
    original_image = st.file_uploader(label="Upload your image", type=["jpg"])

    st.text(" ")

    pixel_size = st.select_slider(
        label="Select the output pixel size of your pixelated image",
        value=5,
        options=[i for i in range(2, 11)],
    )

    palette = st.selectbox(
        label = "Select your color palette",options=["No palette", *pixelator.get_palettes("RGB").keys()], index=None
    )
    if palette == "No palette":
        palette = ""
    else:
        palette = str(palette)

    # Initialize session state if not set
    if "pixelated_image" not in st.session_state:
        st.session_state.pixelated_image = None
    if "show_preview" not in st.session_state:
        st.session_state.show_preview = False


    @st.cache_data(show_spinner=False)
    def pixelate(image, pixel_size, palette):
        return pixelator.pixelate(image, pixel_size, palette)

    if st.button("Pixelate"):
        if original_image is not None:
            with st.spinner("Pixelating image..."):
                st.session_state.pixelated_image = pixelate(original_image, pixel_size, palette)
            st.session_state.show_preview = True
            st.success("Image pixelated successfully!")
        else:
            st.warning("Please upload an image first.")

    # if st.button("Preview"):
    #     # if st.session_state.pixelated_image is not None:
    #     #     st.session_state.show_preview = True
    #     else:
    #         st.warning("Please pixelate an image first.")

with col2:
    st.write("Image preview")

    if st.session_state.show_preview and st.session_state.pixelated_image is not None:
        st.image(st.session_state.pixelated_image)


# # Pixelate
# if original_image:

    # with st.status("Pixelating..."):
    #     pixelated_image = pixelator.pixelate(original_image, pixel_size, palette)

    # st.image(pixelated_image)

    # # Save the pixelated image to a temporary binary stream and
    # # retrieve it from there to download. Workaround to access files
    # # from st.file_uploader.

    # temp_buffer = BytesIO()
    # pixelated_image.save(temp_buffer, format="JPEG")
    # buffered_image = temp_buffer.getvalue()



    # st.download_button(
    #     label="Download",
    #     data=buffered_image,
    #     file_name="pixelator.jpg",
    #     mime="image/jpeg",
    # )


st.divider()

palettes = pixelator.get_palettes("RGB")
palette_names = list(palettes)

col3, col4 = st.columns(2, gap="large")

first_half_of_palettes = palette_names[:math.ceil(len(palette_names)/2)]
second_half_of_palettes = palette_names[math.ceil(len(palette_names)/2):]


with col3:
    first_half_of_palette_dicts = {key: palettes[key] for key in first_half_of_palettes}

    for palette_name, palette in first_half_of_palette_dicts.items():
        with st.expander(f"**{palette_name}**"):
            fig = draw_palette(palette_name, palette)
            st.pyplot(fig, use_container_width=False)

    print("---")


with col4:
    second_half_of_palette_dicts = {key: palettes[key] for key in second_half_of_palettes}

    for palette_name, palette in second_half_of_palette_dicts.items():
        with st.expander(f"**{palette_name}**"):
            fig = draw_palette(palette_name, palette)
            st.pyplot(fig, use_container_width=False)


print("-------------------")


testlist = ["a", "b", "c", "d", "e"]
print(testlist[:3])
print(testlist[3:])