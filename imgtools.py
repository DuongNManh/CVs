import os
from PIL import Image

def load_image(img_path):
    """
        Returns: Image object.
    """
    try:
        img = Image.open(img_path)
        return img
    except Exception as e:
        print("Error at reading img file: ", img_path," ", e)
        return None

def is_image_file(file_path):
    """
        return: True - neu la anh
                False - neu ko phai
    """
    extensions = (".jpg",".png",".jpeg",".bmp",".gif")
    return file_path.lower().endswith(extensions)

def get_image_list(folder_path):
    """
        return Image object list.
    """
    image_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and is_image_file(file):
                img = load_image(file_path)
                image_list.append(img)
    return image_list
            
    