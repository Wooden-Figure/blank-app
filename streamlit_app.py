import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Title of the application
st.title("CVG 110 Labor Plan")

# Instructions
st.write("This is the CVG 110 labor plan. Look at the images below to find your station. You can upload screenshots from your local computer to share them.")

# Google Drive direct download link for predefined image
image_url = "https://drive.google.com/uc?export=download&id=1H-DsYQ7wgtUkyGY72u3oFrQV0Jlr_IHu"

# Display the predefined image "AP prepceive"
st.write("Here is the predefined image 'AP prepceive':")
response = requests.get(image_url)
ap_prepceive_image = Image.open(BytesIO(response.content))
st.image(ap_prepceive_image, caption='AP prepceive', use_column_width=True)

# File uploaders for the 8 stations/images
uploaded_files = st.file_uploader("Choose screenshots for your stations (up to 8)", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    if len(uploaded_files) > 8:
        st.warning("You can upload up to 8 images only.")
    else:
        for idx, uploaded_file in enumerate(uploaded_files):
            # Open the uploaded image file
            image = Image.open(uploaded_file)
            
            # Display the uploaded image
            st.image(image, caption=f'Station {idx + 1}', use_column_width=True)
            
            # Option to download the image
            st.download_button(
                label=f"Download Station {idx + 1} Image",
                data=uploaded_file.getvalue(),
                file_name=uploaded_file.name,
                mime="image/png"
            )

# Note
st.write("Note: Only PNG, JPG, and JPEG files are supported.")
