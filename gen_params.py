import json

# The parameters file should have the same name as the picture, but with
# a .txt extension instead of .jpg.
picture_name = input('Picture name: ')
filename = picture_name + '.txt'

# If the file exists, reuse all the parameters except the current bozzcoins
# Else prompt the user for the parameters.
try:
    with open(filename, 'r') as infile:
        parameters = json.load(infile)
        random_seed = parameters['random_seed']
        target = parameters['target']
        cell_width, cell_height = parameters['cell_size']
except:
    random_seed = input('Random seed: ')
    random_seed = int(random_seed)
    target = input('Target bozzcoins: ')
    target = int(target)
    cell_width = input('Cell width: ')
    cell_width = int(cell_width)
    cell_height = input('Cell height: ')
    cell_height = int(cell_height)

bozzcoins = input('Current bozzcoins: ')
bozzcoins = int(bozzcoins)

# Write picture parameters to file.
with open(filename, 'w') as outfile:
    params = { 'cell_size': [cell_width, cell_height], 'random_seed': random_seed, 'target': target, 'bozzcoins': bozzcoins}
    json.dump(params, outfile)
