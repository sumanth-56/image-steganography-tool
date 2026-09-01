import streamlit as st
from PIL import Image
import io

# --- CORE LOGIC ---
def text_to_binary(text):
    return ''.join([format(ord(char), "08b") for char in text])

def encode_image(image, secret_text):
    image = image.convert("RGB")
    pixels = image.load()
    secret_text += "#####" # delimiter
    binary_message = text_to_binary(secret_text)
    data_index = 0
    message_len = len(binary_message)
    width, height = image.size

    for y in range(height):
        for x in range(width):
            if data_index < message_len:
                r, g, b = pixels[x, y]
                if data_index < message_len:
                    r = (r & ~1) | int(binary_message[data_index])
                    data_index += 1
                if data_index < message_len:
                    g = (g & ~1) | int(binary_message[data_index])
                    data_index += 1
                if data_index < message_len:
                    b = (b & ~1) | int(binary_message[data_index])
                    data_index += 1
                pixels[x, y] = (r, g, b)
            else:
                break
    return image

def decode_image(image):
    image = image.convert("RGB")
    pixels = image.load()
    width, height = image.size
    binary_stream = ""
    decoded_text = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_stream += str(r & 1)
            binary_stream += str(g & 1)
            binary_stream += str(b & 1)

            while len(binary_stream) >= 8:
                byte = binary_stream[:8]
                binary_stream = binary_stream[8:]
                decoded_text += chr(int(byte, 2))
                if decoded_text.endswith("#####"):
                    return decoded_text[:-5]
    return "No hidden message found."

# --- STREAMLIT UI ---
st.set_page_config(page_title="Steganography Tool", page_icon="🕵️")
st.title("Secure Image Steganography 🕵️")
st.write("Hide secret messages inside your images using LSB algorithm.")

tab1, tab2 = st.tabs(["🔒 Hide a Message", "🔓 Read a Message"])

# TAB 1: ENCODE
with tab1:
    st.header("Encode Message")
    upload_encode = st.file_uploader("Upload a PNG Image", type=["png"], key="encode_upload")
    secret_text = st.text_area("Enter your secret message:")
    
    if st.button("Hide Message") and upload_encode and secret_text:
        img = Image.open(upload_encode)
        with st.spinner("Encrypting..."):
            encoded_img = encode_image(img, secret_text)
            
            # Convert image to bytes so user can download it
            buf = io.BytesIO()
            encoded_img.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.success("Message hidden successfully!")
            st.download_button(
                label="Download Secret Image",
                data=byte_im,
                file_name="secret_image.png",
                mime="image/png"
            )

# TAB 2: DECODE
with tab2:
    st.header("Decode Message")
    upload_decode = st.file_uploader("Upload Image to Decode", type=["png"], key="decode_upload")
    
    if st.button("Read Message") and upload_decode:
        img_to_decode = Image.open(upload_decode)
        with st.spinner("Decrypting..."):
            hidden_message = decode_image(img_to_decode)
            
            if hidden_message == "No hidden message found.":
                st.warning(hidden_message)
            else:
                st.success("Message Found!")
                st.info(hidden_message)