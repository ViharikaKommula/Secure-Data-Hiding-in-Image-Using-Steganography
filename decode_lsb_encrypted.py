from PIL import Image
import numpy as np
from cryptography.fernet import Fernet

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

def decode_lsb(image_path, key):
    image = Image.open(image_path)
    image = image.convert('RGB')
    binary_data = ''

    pixels = np.array(image)
    for row in pixels:
        for pixel in row:
            for channel in range(3):
                binary_data += format(pixel[channel], '08b')[-1]

    # Split by 8 bits and stop at the end marker
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    encrypted_data = bytearray()
    for byte in all_bytes:
        if byte == '11111111':  # End marker
            break
        encrypted_data.append(int(byte, 2))

    return decrypt_message(bytes(encrypted_data), key)