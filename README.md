# Secure-Data-Hiding-in-Image-Using-Steganography

**********Introduction**********

This project presents a steganography application that securely conceals data within images using the Least Significant Bit (LSB) technique, enhanced with encryption. By encrypting messages prior to embedding, the tool provides an additional security layer, ensuring sensitive information remains confidential. Featuring an intuitive interface, it supports various image formats and offers options for image processing, such as grayscale and blur.

**********Key Features**********

Secure Encryption: Employs Fernet encryption to protect messages before embedding.

Format Compatibility: Works with PNG, JPG, and BMP image types.

Intuitive Interface: Easy-to-use GUI for straightforward encoding and decoding.

Image Effects: Options to apply grayscale and blur to images.

Capacity: Can embed messages up to 128 characters long.

Accurate Retrieval: Uses an end marker for precise message extraction.

Minimal Impact: Ensures image quality is preserved.

Error Management: Effectively handles incorrect inputs and formats.

Functionality

Encoding: Encrypts and embeds messages in images, with optional grayscale or blur effects.

Decoding: Extracts and decrypts messages from encoded images.

Key Handling: Generates and utilizes a unique encryption key for secure message processing.

Visual Effects: Offers options to apply visual modifications to the encoded image.

**Implementation Details**

Setup:

Ensure Python is installed on your machine.
Install necessary libraries using pip:

pip install opencv-python numpy pillow cryptography

**Using the Application:**

Run main.py to open the GUI.

Select an image file using the "Browse" button.
Enter the message to encode and click "Encode" to embed it in the image.
Save the displayed encryption key for decoding.
To decode, provide the path to the encoded image and the encryption key, then click "Decode."

**Code Organization:**

main.py: Initiates the GUI.

encode_lsb_encrypted.py: Manages message encryption and embedding.

decode_lsb_encrypted.py: Handles message extraction and decryption.

gui.py: Offers the graphical interface for user interaction.
