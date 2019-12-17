import sys

def day8():
    filepath = "day8.in"
    with open(filepath) as fp:
        picture = fp.readline().strip()

        WIDTH = 25
        HEIGHT = 6
        SIZE = WIDTH * HEIGHT

        layers = []
        layer_count = count = 0
        
        # Format input into layers
        while count < len(picture):
            layers.append([])
            for h in range(0, HEIGHT):
                layers[layer_count].append([])
                for w in range(0, WIDTH):
                    layers[layer_count][h].append(picture[count])
                    count += 1
            layer_count += 1

        # Find the layer with the smallest number of zeros
        min_zeros = sum(layer.count('0') for layer in layers[0])
        min_layer = layers[0]

        for layer in layers:
            num_zeros = sum(sub_layer.count('0') for sub_layer in layer)
            if num_zeros < min_zeros:
                min_zeros = num_zeros
                min_layer = layer

        num_ones = sum(sub_layer.count('1') for sub_layer in min_layer)
        num_twos = sum(sub_layer.count('2') for sub_layer in min_layer)
        ans =  num_ones * num_twos
        print("Part 1: " + str(ans))

        # Part 2
        print("Part 2:")

        # Figure out which pixel colour will be seen
        for h in range(0, HEIGHT):
            for w in range(0, WIDTH):
                for layer in layers:
                    if layer[h][w] != '2':
                        sys.stdout.write('1') if layer[h][w] == '1' else sys.stdout.write(' ')
                        break
            print('\n')

if __name__ == '__main__':
    day8()