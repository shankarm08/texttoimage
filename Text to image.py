import streamlit as st
import openai
from IPython.display import Image

# Set your OpenAI API key
openai.api_key = ""

# Function to generate image based on text prompt
def generate_image(prompt, size="512x512"):
    response = openai.Image.create(
        prompt=prompt,
        n=1,  # Number of images to generate
        size=size  # Size of the generated image
    )
    image_url = response['data'][0]['url']
    return image_url

# Streamlit app
def main():
    st.title("Text to Image Generator")

    # Input text prompt
    text_input = st.text_input("Enter text prompt:", "cats")

    # Generate image when user clicks the button
    if st.button("Generate Image"):
        image_url = generate_image(text_input)
        st.image(image_url, caption="Generated Image", use_column_width=True)

if __name__ == "__main__":
    main()
