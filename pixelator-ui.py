import streamlit as st


pg = st.navigation(
    [
        st.Page("page_1.py", title="Pixelator", default=True),
        st.Page("page_2.py", title="Palette Overview (df)"),
        st.Page("page_3.py", title="Palette Overview (plt)"),
    ]
)

pg.run()
