import json

#TODO: Get parameters from the command line
f = open('prata-bozz.txt', 'w')
params = { 'cell_size': [20, 20], 'random_seed': 797, 'target': 12000, 'bozzcoins': 797}
json.dump(params, f)
