#!/usr/bin/python3

from PIL import Image, ImageDraw
import random
import json

BORDER_THICKNESS = 1
CELL_COLOUR = "gray"
BORDER_COLOUR = "black"
PICTURE_FILENAME = 'prata-bozz.jpg'

def read_picture_parameters(filename):
    parameters = {}
    with open(filename, 'r') as infile:
        parameters = json.load(infile)
    return parameters

# Draw a single cell to hide the image at the given cell number
# Cells are numbered left to right, top to bottom.
def overlay_cell(image_drawer, cell_number, parameters):
    cell_row = cell_number // parameters['cell_counts'][0]
    cell_column = cell_number % parameters['cell_counts'][0]
    draw_cell(image_drawer, (cell_column * parameters['cell_size'][0], cell_row * parameters['cell_size'][1]), parameters['cell_size'])

def draw_cell(image_drawer, top_left_coordinate, size):
    # Draw outer box, full cell.
    bottom_right_coordinate = (top_left_coordinate[0] + size[0], top_left_coordinate[1] + size[1])
    image_drawer.rectangle((top_left_coordinate, bottom_right_coordinate), fill=BORDER_COLOUR)
    # Draw inner box, so the outer box forms the border.
    inner_top_left = (top_left_coordinate[0] + BORDER_THICKNESS, top_left_coordinate[1] + BORDER_THICKNESS)
    inner_bottom_right = (bottom_right_coordinate[0] - BORDER_THICKNESS, bottom_right_coordinate[1] - BORDER_THICKNESS)
    image_drawer.rectangle((inner_top_left, inner_bottom_right), fill=CELL_COLOUR)

image = Image.open(PICTURE_FILENAME)
parameters_filename = PICTURE_FILENAME.split('.')[0] + '.txt'
parameters = read_picture_parameters(parameters_filename)
parameters['width'], parameters['height'] = image.size
parameters['cell_counts'] = (parameters['width'] // parameters['cell_size'][0], parameters['height'] // parameters['cell_size'][1])
print(parameters)
draw = ImageDraw.Draw(image)
parameters['bozzcoins'] = 807

num_total_cells = parameters['cell_counts'][0] * parameters['cell_counts'][1]
num_coins_per_cell = parameters['target'] // num_total_cells
num_covered_cells = num_total_cells - parameters['bozzcoins'] // num_coins_per_cell

random.seed(parameters['random_seed'])
covered_cells = random.sample(range(num_total_cells), num_covered_cells)

for cell_number in covered_cells:
    overlay_cell(draw, cell_number, parameters)

image.save(PICTURE_FILENAME.split('.')[0] + '-obfuscated.jpg')
