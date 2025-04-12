# Pixelator

## Create pixel art from any image

I really like the 8-bit aesthetics of retro gaming consoles and pixel art in general, so I decided to do this little project that allows me to create pixel art from basically any image. Users can choose the size of the output pixels and apply various color palettes. Here are some images of the pixelator in action:

<table>
  <tr>
    <td><img src="https://github.com/thomasjenny/pixelator/blob/main/examples/01_original.jpg" width="320"></td>
    <td><img src="https://github.com/thomasjenny/pixelator/blob/main/examples/01_pixelated.jpg" width="320"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/thomasjenny/pixelator/blob/main/examples/02_original.jpg" width="320"></td>
    <td><img src="https://github.com/thomasjenny/pixelator/blob/main/examples/02_pixelated.jpg" width="320"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/thomasjenny/pixelator/blob/main/examples/03_original.jpg" width="320"></td>
    <td><img src="https://github.com/thomasjenny/pixelator/blob/main/examples/03_pixelated.jpg" width="320"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/thomasjenny/pixelator/blob/main/examples/04_original.jpg" width="320"></td>
    <td><img src="https://github.com/thomasjenny/pixelator/blob/main/examples/04_pixelated.jpg" width="320"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/thomasjenny/pixelator/blob/main/examples/05_original.jpg" width="320"></td>
    <td><img src="https://github.com/thomasjenny/pixelator/blob/main/examples/05_pixelated.jpg" width="320"></td>
  </tr>
</table>


## How to use

Step 1: Clone the repo
```
git clone https://github.com/thomasjenny/pixelator.git
```

Step 2: Install requirements
```
pip install -r requirements.txt
```

Step 3: Create a Pixelator instance, define an input path, pixelate, and preview the result with `show_image()`. If you want to save the result, specify a path and a filename and use `save_image()`
```
from pixelator import Pixelator
pixelator = Pixelator()

in_path = "examples/01_original.jpg"
pixelator.pixelate(in_path, 3, "shimmering_sunset")
pixelator.show_image()

out_path = "examples"
out_name = "01_test.jpg"
pixelator.save_image(out_path, out_name)
```

**Or alternatively:** use the GUI
```
streamlit run app.py
```


## Streamlit GUI

![Screenshot of the Pixelator Streamlit GUI](/assets/streamlit_screenshot.png)


## Image Credits

* Photo by [cody reed](https://unsplash.com/@editable_edits) on [Unsplash](https://unsplash.com/photos/a-red-sports-car-parked-in-a-parking-lot-SyG3Xf_ZxfM)
* Photo by [Debby Hudson](https://unsplash.com/@hudsoncrafted) on [Unsplash](https://unsplash.com/photos/blue-house-photography-FmCSSSGge-0)
* [Katsushika Hokusai - Thirty-Six Views of Mount Fuji- The Great Wave Off the Coast of Kanagawa - Google Art Project.jpg](https://commons.wikimedia.org/wiki/File:Katsushika_Hokusai_-_Thirty-Six_Views_of_Mount_Fuji-_The_Great_Wave_Off_the_Coast_of_Kanagawa_-_Google_Art_Project.jpg), public domain 
* Photo by [Johann Siemens](https://unsplash.com/@emben) on [Unsplash](https://unsplash.com/photos/green-tree-on-grassland-during-daytime-EPy0gBJzzZU)
* Photo by [Daniel Monteiro](https://unsplash.com/@danielmonteirox) on [Unsplash](https://unsplash.com/photos/woman-looking-back-37uZlXLYpGo)