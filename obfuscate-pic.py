#!/usr/bin/python3

from PIL import Image, ImageDraw
import random

BORDER_THICKNESS = 1
CELL_SIZE = (20, 20)
CELL_COLOUR = "white"
BORDER_COLOUR = "black"

# Draw a single cell to hide the image at the given cell number
# Cells are numbered left to right, top to bottom.
def overlay_cell(image_drawer, cell_number, cell_counts):
    cell_row = cell_number // cell_counts[0]
    cell_column = cell_number % cell_counts[0]
    draw_cell(image_drawer, (cell_column * CELL_SIZE[0], cell_row * CELL_SIZE[1]), CELL_SIZE)

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
# Number of cells. Tuple with (number of columns, number of rows).
cell_counts = (width // CELL_SIZE[0], height // CELL_SIZE[1])
draw = ImageDraw.Draw(image)

for i in range(30, 60):
    overlay_cell(draw, i, cell_counts)

image.save("prata-bozz-obfuscated.jpg")
