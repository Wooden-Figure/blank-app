import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Title of the application
st.title("CVG 110 Labor Plan")

# Instructions
st.write("This is the CVG 110 labor plan. You can upload a screenshot from your local computer to share it.")

# Google Drive direct download link
image_url = "https://drive.google.com/uc?export=download&id=1H-DsYQ7wgtUkyGY72u3oFrQV0Jlr_IHu"

# Display the predefined image "AP prepceive"
st.write("Here is the predefined image 'AP prepceive':")
response = requests.get(image_url)
ap_prepceive_image = Image.open(BytesIO(response.content))
st.image(ap_prepceive_image, caption='AP prepceive', use_column_width=True)

# File uploader for the screenshot
uploaded_file = st.file_uploader("Choose a screenshot file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image file
    image = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(image, caption='Uploaded Screenshot', use_column_width=True)
    
    # Option to download the image
    st.download_button(
        label="Download Image",
        data=uploaded_file.getvalue(),
        file_name=uploaded_file.name,
        mime="image/png"
    )

# Note
st.write("Note: Only PNG, JPG, and JPEG files are supported.")
