import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Title of the application
st.title("CVG 110 Labor Plan")

# Instructions
st.write("This is the CVG 110 labor plan. Look at the images below to find your station.")

# List of Google Drive direct download links for the images
image_urls = [
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_1",
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_2",
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_3",
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_4",
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_5",
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_6",
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_7",
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_8"
]

# Display images from Google Drive links
for idx, image_url in enumerate(image_urls):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    st.image(image, caption=f'Station {idx + 1}', use_column_width=True)
    st.download_button(
        label=f"Download Station {idx + 1} Image",
        data=response.content,
        file_name=f'Station_{idx + 1}.png',
        mime="image/png"
    )

# Note
st.write("Note: Only PNG, JPG, and JPEG files are supported.")
