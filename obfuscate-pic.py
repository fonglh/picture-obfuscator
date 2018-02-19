#!/usr/bin/python3

from PIL import Image, ImageDraw
import random

BORDER_THICKNESS = 1
SIZE = (20, 20)
CELL_COLOUR = "white"
BORDER_COLOUR = "black"

# Draw a single cell to hide the image at the given cell number
def overlay_cell(image_drawer, cell_number):
    pass

def draw_cell(image_drawer, top_left_coordinate, size):
    # Draw outer box, full cell.
    bottom_right_coordinate = (top_left_coordinate[0] + size[0], top_left_coordinate[1] + size[1])
    image_drawer.rectangle((top_left_coordinate, bottom_right_coordinate), fill=BORDER_COLOUR)
    # Draw inner box, so the outer box forms the border.
    inner_top_left = (top_left_coordinate[0] + BORDER_THICKNESS, top_left_coordinate[1] + BORDER_THICKNESS)
    inner_bottom_right = (bottom_right_coordinate[0] - BORDER_THICKNESS, bottom_right_coordinate[1] - BORDER_THICKNESS)
    image_drawer.rectangle((inner_top_left, inner_bottom_right), fill=CELL_COLOUR)

image = Image.open("prata-bozz.jpg")
width, height = image.size
draw = ImageDraw.Draw(image)

for x in range(width//SIZE[0]):
    for y in range(height//SIZE[1]):
        if random.randint(1, 100) > 65:
            draw_cell(draw, (x * SIZE[0], y * SIZE[1]), SIZE)

image.save("prata-bozz-obfuscated.jpg")
