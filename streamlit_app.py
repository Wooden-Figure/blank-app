import streamlit as st
from PIL import Image
import os

# Title of the application
st.title("Screenshot Sharing Application")

# Instructions
st.write("Upload a screenshot from your local computer to share it.")

# Path to the predefined image "AP prepceive"
# Update the path to point to your desktop
image_path = "C:/Users/Buddy/Desktop/AP prepceive.png"

if os.path.exists(image_path):
    # Display the predefined image "AP prepceive"
    st.write("Here is the predefined image 'AP prepceive':")
    ap_prepceive_image = Image.open(image_path)  # Ensure the image is in the same directory as this script
    st.image(ap_prepceive_image, caption='AP prepceive', use_column_width=True)
else:
    st.write("The predefined image 'AP prepceive' is not found. Please check the file path.")

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
