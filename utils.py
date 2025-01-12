import json
import pandas as pd


def load_palettes(path: str = "assets/palettes_hex.json"):
    """Load all coloro palletes and return the hex values"""
    with open(path) as file:
        palettes = json.load(file)
        return palettes


def generate_color_dfs():
    """Return a dict that contains the palette name (key) and a 5-column
    wide dataframe with all hex values (value)
    """
    palettes = load_palettes()
    palettes_dict = {}

    for name, palette in palettes.items():
        tab = []

        for i in range(0, len(palette), 5):
            tab.append(palette[i : i + 5])

        df = pd.DataFrame(tab)

        palettes_dict[name] = df

    return palettes_dict


def style_color_df(df):
    """Return a styling dataframe containing CSS to color each cell with
    the corresponding hex value. Must be applied to the original datafame.
    """
    newtab = []
    for index, row in df.iterrows():
        newrow = []
        for cell in row:
            style = f"background-color: {cell}"
            newrow.append(style)
        newtab.append(newrow)
    newdf = pd.DataFrame(newtab)

    return newdf


if __name__ == "__main__":
    palettes = generate_color_dfs()
    # print(palettes)

    p8 = palettes["pico-8"]
    # print(p8)
    # print(type(p8))

    styletest = style_color_df(p8)
    print(styletest)
