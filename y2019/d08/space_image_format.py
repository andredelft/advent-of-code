from itertools import batched
from lib.math import product
from lib.field import Field


def parse_input(input_string, sizes):
    return list(batched(input_string, product(sizes)))


def solve_a(input_string, sizes=(6, 25)):
    layers = parse_input(input_string, sizes)

    min_zeros = None
    min_zeros_layer_index = None

    for i, layer in enumerate(layers):
        num_zeros = len([n for n in layer if n == "0"])

        if (min_zeros == None) or (min_zeros > num_zeros):
            min_zeros = num_zeros
            min_zeros_layer_index = i

    min_zeros_layer = layers[min_zeros_layer_index]
    return len([n for n in min_zeros_layer if n == "1"]) * len(
        [n for n in min_zeros_layer if n == "2"]
    )


def solve_b(input_string, sizes=(6, 25)):
    layers = parse_input(input_string, sizes)
    layers = [list(batched(layer, sizes[1])) for layer in layers]
    print(layers)
    final_image = Field.blank(*sizes)

    for j, i in final_image.coords():
        layer_index = 0
        value = layers[0][j][i]

        while value == "2":
            layer_index += 1
            value = layers[layer_index][j][i]

        final_image[j, i] = "X" if value == "1" else " "

    return str(final_image)
