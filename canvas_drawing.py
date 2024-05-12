# canvas_drawing.py
from PIL import Image, ImageDraw

def create_canvas():
    canvas_size = (300, 300)
    return Image.new("RGB", canvas_size, color="white")

def user_drawing(canvas):
    # Thực hiện các thao tác vẽ của người dùng, ví dụ như vẽ elip:
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((50, 50, 100, 100), fill="blue")

def save_canvas(canvas):
    canvas.save("drawn_picture.jpg")