import cv2
import numpy as np
from PIL import Image
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def encode_lsb(image_path, data, key):
    encrypted_data = encrypt_message(data, key)
    binary_data = ''.join(format(byte, '08b') for byte in encrypted_data) + '1111111111111110'  # End marker
    data_index = 0
    data_length = len(binary_data)

    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = np.array(image)

    for row in pixels:
        for pixel in row:
            for channel in range(3): 
                if data_index < data_length:
                    pixel[channel] = int(format(pixel[channel], '08b')[:-1] + binary_data[data_index], 2)
                    data_index += 1
                if data_index >= data_length:
                    break

    encoded_image = Image.fromarray(pixels)
    encoded_image_path = r'C:\stego_project\images\encoded_image.png'
    encoded_image.save(encoded_image_path)
    return encoded_image_path
