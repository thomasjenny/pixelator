import streamlit as st
from utils import create_styling_df, generate_color_dfs

st.title("Color palette overview")

palettes = generate_color_dfs()

for palette_name, palette in palettes.items():
    style_df = create_styling_df(palette)
    styled_palette_df = palette.style.apply(lambda x: style_df, axis=None)
    st.write(palette_name)
    st.dataframe(styled_palette_df)
