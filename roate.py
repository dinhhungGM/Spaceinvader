from PIL import Image
import os


images = [Image.open(os.path.join("image", file)) for file in os.listdir(os.path.join("image"))]

