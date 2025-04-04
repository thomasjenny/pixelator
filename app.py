from io import BytesIO
import math
import streamlit as st

from pixelator import Pixelator
from utils import draw_palette


st.set_page_config(layout="wide")


pixelator = Pixelator()


st.title("Pixelator")
st.subheader("Create pixel art from any image!")


col1, col2, col3 = st.columns(3, gap="large")

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
        label="Select your color palette",
        options=["No palette", *pixelator.get_palettes("RGB").keys()],
        index=None,
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
                st.session_state.pixelated_image = pixelate(
                    original_image, pixel_size, palette
                )
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
    st.write("Original image")

    if original_image:
        st.image(original_image)

with col3:
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




st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.subheader("Color Palettes Preview")

palettes = pixelator.get_palettes("RGB")
palette_names = list(palettes)
palettes_to_plot = math.ceil(len(palette_names) / 4)


palette_col1, palette_col2, palette_col3, palette_col4 = st.columns(4, gap="large", border=True)

palette_column_1 = palette_names[:palettes_to_plot]
palette_column_2 = palette_names[palettes_to_plot : palettes_to_plot * 2]
palette_column_3 = palette_names[palettes_to_plot * 2 : palettes_to_plot * 3]
palette_column_4 = palette_names[palettes_to_plot * 3 :]


with palette_col1:
    col1_palettes = {key: palettes[key] for key in palette_column_1}
    for palette_name, palette in col1_palettes.items():
        fig = draw_palette(palette_name, palette)
        st.pyplot(fig, use_container_width=False)

with palette_col2:
    col2_palettes = {key: palettes[key] for key in palette_column_2}
    for palette_name, palette in col2_palettes.items():
        fig = draw_palette(palette_name, palette)
        st.pyplot(fig, use_container_width=False)

with palette_col3:
    col2_palettes = {key: palettes[key] for key in palette_column_3}
    for palette_name, palette in col2_palettes.items():
        fig = draw_palette(palette_name, palette)
        st.pyplot(fig, use_container_width=False)

with palette_col4:
    col2_palettes = {key: palettes[key] for key in palette_column_4}
    for palette_name, palette in col2_palettes.items():
        fig = draw_palette(palette_name, palette)
        st.pyplot(fig, use_container_width=False)


with st.expander("Color Palettes Credits"):
    st.markdown(
        """[Sweetie 16](https://lospec.com/palette-list/sweetie-16) palette by GrafxKid  
        [Better16](https://lospec.com/palette-list/better16) palette by [PG](https://lospec.com/pg)  
        [Pico-8](https://lospec.com/palette-list/pico-8) palette 
        by [Pico-8](https://www.lexaloffle.com/pico-8.php)  
        [AAP-64](https://lospec.com/palette-list/aap-64) palette 
        by [Adigun A. Polack](https://lospec.com/adigunpolack)  
        [Shimmering Sunset](https://lospec.com/palette-list/shimmering-sunset) palette
        by [sillyTheJester](https://lospec.com/sillythejester)  
        [Sorbet Special](https://lospec.com/palette-list/sorbet-special) palette 
        by [Qirlfriend](https://lospec.com/qirlfriend)  
        [Undernight 20](https://lospec.com/palette-list/undernight-20) palette
        by [yedamameday](https://lospec.com/yedamameday)  
        [BLK RX64](https://lospec.com/palette-list/blk-nx64) palette
        by [BurakoIRL](https://lospec.com/blkirl)  
        [Chasm](https://lospec.com/palette-list/chasm) palette 
        by [dysphoriaa](https://lospec.com/dysphoriaa)  
        [Blood Moon](https://lospec.com/palette-list/blood-moon) palette
        by [BaguetteCat](https://lospec.com/no-name5)  
        [Slicko-8](https://lospec.com/palette-list/slicko-8) palette 
        by [cptn.piranha](https://lospec.com/cptnpiranha)  
        [Candy Heart](https://lospec.com/palette-list/candy-heart) palette
        by [pixel rubik cube](https://lospec.com/pixelrubikcube)
        """
    )
