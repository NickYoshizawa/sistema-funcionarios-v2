from customtkinter import CTkImage
from PIL import Image
import numpy as np


def open_image(path: str, size: tuple = (16, 16)):
    try:
        image = Image.open(path)
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        np_image = np.array(image)
        np_image[:, :, :3] = 255
        result_image = Image.fromarray(np_image)
        modified_image = CTkImage(result_image, size=size)
        return modified_image
    except Exception as e:
        print(f"Failed to process image: {e}")