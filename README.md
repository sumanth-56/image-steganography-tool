# 🕵️‍♂️ Secure Image Steganography Tool (LSB)

**🚀 [Click here to try the Live Web App!](https://image-steganography-tool-amfswmxmbqh4nkuwf7useu.streamlit.app/)**

## Overview
A full-stack web application and CLI tool that hides secret text messages inside images using the **Least Significant Bit (LSB)** cryptographic algorithm. The tool modifies pixel data at a binary level, ensuring the hidden data creates absolutely no visual distortion to the human eye. 

⚠️ **Note on Image Formats:** This tool strictly requires **`.png`** images. PNG uses lossless compression, which preserves the exact binary pixel values required for data retrieval. Lossy formats like JPG alter pixel data and will corrupt the hidden message.

## Features
* **Web UI Deployment:** Fully deployed interactive web interface built with Streamlit.
* **Pixel-Level Encryption:** Embeds secret text directly into RGB channels using bitwise manipulation `(r & ~1) | bit`.
* **Optimized Decryption:** Retrieves hidden text with an optimized early-exit stream processing algorithm, drastically reducing latency on high-resolution images.
* **Data Integrity:** Enforces lossless `.png` processing to prevent artifact corruption.

## Technology Stack
* **Language:** Python 3.x
* **Frontend/Deployment:** Streamlit, Streamlit Community Cloud
* **Image Processing:** Pillow (PIL)
* **Core Logic:** Binary Manipulation, Bitwise Operations

## How to Run Locally

### 1. Web Interface (Streamlit)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the web app
streamlit run app.py
