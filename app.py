from io import BytesIO
import streamlit as st

from pixelator import Pixelator
from utils import draw_palette


st.set_page_config(layout="wide")

# Initialize session state
if "pixelated_image" not in st.session_state:
    st.session_state.pixelated_image = None
if "show_preview" not in st.session_state:
    st.session_state.show_preview = False
if "palettes_plots" not in st.session_state:
    st.session_state.palettes_plots = None

# Initialize Pixelator instance
pixelator = Pixelator()


# Helper function for pixelating images and caching the result
@st.cache_data(show_spinner=False)
def pixelate(image, pixel_size, palette):
    return pixelator.pixelate(image, pixel_size, palette)


# Helper function for plotting the color palettes and caching the plots
@st.cache_data(show_spinner=False)
def plot_palettes(palettes):
    for palette_name, palette in palettes.items():
        st.write(palette_name)
        fig = draw_palette(palette_name, palette)
        st.pyplot(fig, use_container_width=True)
        st.divider()


# App layout
st.title("Pixelator")
st.subheader("Create pixel art from any image!")
st.write(" ")
st.write(" ")

col1, col2, col3 = st.columns(3, gap="large")

# Inputs
with col1:
    st.write("Upload your image")
    original_image = st.file_uploader(
        label="Upload your image", type=["jpg"], label_visibility="collapsed"
    )
    st.write(" ")

    st.write("Select your output pixel size")
    pixel_size_input = st.select_slider(
        label="Select the output pixel size of your pixelated image",
        value=5,
        options=[i for i in range(2, 11)],
        label_visibility="collapsed"
    )
    st.write(" ")

    st.write("Select your color palette")
    palette_input = st.selectbox(
        label="Select your color palette",
        options=["No palette", *pixelator.get_palettes("RGB").keys()],
        index=None,
        label_visibility="collapsed"
    )
    palette = "" if palette_input == "No palette" else str(palette_input)
    st.text(" ")

    # Pixelate button - check if an image has been uploaded. If yes,
    # pixelate and set show_preview session state to True. This is
    # needed in col3 to display the pixelated image (if one is available)
    if st.button(label="Pixelate!", use_container_width=True):
        if original_image is not None:
            with st.spinner("Pixelating image..."):
                st.session_state.pixelated_image = pixelate(
                    original_image, pixel_size_input, palette_input
                )
            st.session_state.show_preview = True
            st.success("Image pixelated successfully!")
        else:
            st.warning("Please upload an image first.")

# Original image preview (appears as soon as image is uploaded)
with col2:
    st.write("Original image")
    if original_image:
        st.image(original_image)

# Pixelated image preview & download
with col3:
    st.write("Pixelated image preview")
    # Check if session state is set - if yes, display pixelated image
    if st.session_state.show_preview and st.session_state.pixelated_image is not None:
        st.image(st.session_state.pixelated_image)
        st.write(" ")

        # Save image to buffer for download
        temp_buffer = BytesIO()
        st.session_state.pixelated_image.save(temp_buffer, format="JPEG")
        buffered_image = temp_buffer.getvalue()

    # Download button - download buffered image
    if st.session_state.pixelated_image is not None:
        st.download_button(
            label="Download pixelated image",
            data=buffered_image,
            file_name="pixelator.jpg",
            mime="image/jpeg",
            use_container_width=True,
        )


with st.sidebar:
    palettes = pixelator.get_palettes("hex")
    col1, col2, col3 = st.columns([0.5, 2, 0.5])

    with col1:
        st.write("")
    with col2:
        st.markdown("**Color palettes**")
        st.divider()
        plot_palettes(palettes)
        st.write(" ")
    with col3:
        st.write("")

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
