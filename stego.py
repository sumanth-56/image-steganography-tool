from PIL import Image

def text_to_binary(text):
    """Convert text string to a binary string."""
    # ord(char) -> ASCII value
    # format(value, '08b') -> 8-bit binary
    return ''.join([format(ord(char), "08b") for char in text])

def binary_to_text(binary_string):
    """Convert binary string back to text."""
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    return ''.join([chr(int(char, 2)) for char in chars])

def encode_image(image_path, secret_text, output_path):
    # Open the image
    image = Image.open(image_path)
    # Convert image to RGB (Standard Red, Green, Blue)
    image = image.convert("RGB") 
    pixels = image.load()

    # Add a delimiter "#####" so we know when the message stops
    secret_text += "#####"
    binary_message = text_to_binary(secret_text)
    data_index = 0
    message_len = len(binary_message)

    width, height = image.size

    print("Encrypting...")
    
    # Iterate through every pixel
    for y in range(height):
        for x in range(width):
            if data_index < message_len:
                # Get the RGB values (e.g., (100, 255, 12))
                r, g, b = pixels[x, y]

                # Modify the Least Significant Bit (LSB) of Red
                # If we need a '1', make the number odd. If '0', make it even.
                
                # Logic for Red Pixel
                if data_index < message_len:
                    bit = int(binary_message[data_index])
                    # Bitwise operation: clears last bit, then adds our bit
                    r = (r & ~1) | bit 
                    data_index += 1

                # Logic for Green Pixel
                if data_index < message_len:
                    bit = int(binary_message[data_index])
                    g = (g & ~1) | bit
                    data_index += 1

                # Logic for Blue Pixel
                if data_index < message_len:
                    bit = int(binary_message[data_index])
                    b = (b & ~1) | bit
                    data_index += 1

                # Update the pixel with new values
                pixels[x, y] = (r, g, b)
            else:
                break
    
    # Save the new image
    image.save(output_path)
    print(f"Success! Message hidden in {output_path}")

def decode_image(image_path):
    print("Decrypting...")
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = image.load()

    width, height = image.size
    binary_stream = ""
    decoded_text = ""

    # Loop through pixels
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Get LSBs from Red, Green, Blue
            binary_stream += str(r & 1)
            binary_stream += str(g & 1)
            binary_stream += str(b & 1)

            # Every 8 bits, try to form a character
            while len(binary_stream) >= 8:
                # Take the first 8 bits
                byte = binary_stream[:8]
                # Remove them from the stream
                binary_stream = binary_stream[8:] 
                
                # Convert to character
                char = chr(int(byte, 2))
                decoded_text += char

                # CHECK: Did we find the stopper?
                if decoded_text.endswith("#####"):
                    # Stop immediately and return the message!
                    return decoded_text[:-5] 
    
    return "No hidden message found."

if __name__ == "__main__":
    print("--- Invisible Message Tool (Steganography) ---")
    choice = input("Type '1' to Hide a message, or '2' to Read a message: ")

    if choice == '1':
        img_name = input("Enter image filename (e.g., dog.png): ")
        text = input("Enter secret message: ")
        encode_image(img_name, text, "secret_image.png")
    
    elif choice == '2':
        img_name = input("Enter image filename to decode (e.g., secret_image.png): ")
        print("Hidden Message:", decode_image(img_name))
    
    else:
        print("Invalid choice.")