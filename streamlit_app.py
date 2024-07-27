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
    "https://drive.google.com/uc?export=download&id=1H-DsYQ7wgtUkyGY72u3oFrQV0Jlr_IHu",
    '''"https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_2",  # Replace with actual file ID
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_3",  # Replace with actual file ID
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_4",  # Replace with actual file ID
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_5",  # Replace with actual file ID
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_6",  # Replace with actual file ID
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_7",  # Replace with actual file ID
    "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_8"   # Replace with actual file ID'''
]

# Display images from Google Drive links
for idx, image_url in enumerate(image_urls):
    if "YOUR_FILE_ID" in image_url:
        continue  # Skip placeholders

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
st.
