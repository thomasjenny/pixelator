import streamlit as st


pg = st.navigation(
    [
        st.Page("st_main_page.py", title="Pixelator", default=True),
        st.Page("st_palettes_page.py", title="Palette Preview"),
    ]
)

pg.run()
