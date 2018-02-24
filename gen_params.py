import json

# The parameters file should have the same name as the picture, but with
# a .txt extension instead of .jpg.
picture_filename = input('Picture filename with extension: ')
filename = picture_filename.split('.')[0] + '.txt'

# If the file exists, print the parameters.
# Else prompt the user for the parameters.
try:
    with open(filename, 'r') as infile:
        parameters = json.load(infile)
        cell_width, cell_height = parameters['cell_size']
        random_seed = parameters['random_seed']
        target = parameters['target']
        print(parameters)
except:
    random_seed = input('Random seed: ')
    random_seed = int(random_seed)
    target = input('Target bozzcoins: ')
    target = int(target)
    cell_width = input('Cell width: ')
    cell_width = int(cell_width)
    cell_height = input('Cell height: ')
    cell_height = int(cell_height)

# Write picture parameters to file.
with open(filename, 'w') as outfile:
    params = { 'cell_size': [cell_width, cell_height], 'random_seed': random_seed, 'target': target}
    json.dump(params, outfile)
