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
    "https://drive.google.com/uc?export=download&id=1-0wvCDSPuOS4FGVdpkhfVG8jpQ7W4XE3",
    "https://drive.google.com/uc?export=download&id=1H-DsYQ7wgtUkyGY72u3oFrQV0Jlr_IHu",
    # Add more URLs here as needed
]

# Display images from Google Drive links
for idx, image_url in enumerate(image_urls):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        st.image(image, caption=f'Station {idx + 1}', use_column_width=True)
        st.download_button(
            label=f"Download Station {idx + 1} Image",
            data=response.content,
            file_name=f'Station_{idx + 1}.png',
            mime="image/png"
        )
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to load image {idx + 1}: {e}")
    except Image.UnidentifiedImageError:
        st.error(f"Failed to identify image {idx + 1}. The content is not a valid image.")

# Note
st.write("Note: Only PNG, JPG, and JPEG files are supported.")
