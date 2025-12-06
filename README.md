# Image Steganography Tool (LSB)

## Overview
This is a Command Line Interface (CLI) tool capable of hiding secret text messages inside PNG images. It utilizes the **Least Significant Bit (LSB)** algorithm to modify pixel data at a binary level, ensuring the hidden message creates no visual distortion to the human eye.

## Features
* **Encryption:** Embeds text into images using bitwise manipulation.
* **Decryption:** Retrieves hidden text from images with an optimized early-exit algorithm.
* **Security:** Data is hidden at the pixel level, making it invisible to standard image viewers.
* **Performance:** Capable of processing high-resolution images efficiently.

## Prerequisites
* Python 3.x
* Pillow Library (`pip install pillow`)

## How to Run
1. Clone the repository or download `stego.py`.
2. Open your terminal.
3. Run the script:
   ```bash
   python stego.py
