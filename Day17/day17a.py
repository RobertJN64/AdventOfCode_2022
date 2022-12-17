rock_shapes = [
    ['  @@@@ '],

    ['   @   ',
     '  @@@  ',
     '   @   '],

    ['    @  ',
     '    @  ',
     '  @@@  '],

    ['  @    ',
     '  @    ',
     '  @    ',
     '  @    '],

    ['  @@   ',
     '  @@   ']
]

SIM_CONSTANT = 6

def main():
    with open("Day17/day17.txt") as f:
        pattern = f.read().strip()
    p_index = 0

    layers = ['#' * 7]
    TOTAL_ROCKS = 2022
    for rock in range(0, TOTAL_ROCKS):
        print(rock)
        while len(layers) > 4 and layers[-4] == " " * 7:
            layers.pop()
        while len(layers) < 4 or layers[-3] != " " * 7:
            layers.append(" " * 7)

        new_rock = rock_shapes[rock%len(rock_shapes)]
        for layer in new_rock[::-1]:
            layers.append(layer)

        # print()
        # print("+")
        # for item in layers[::-1]:
        #     print('|' + item + '|')
        #input()

        #SIMULATE
        top_layer = len(layers)
        while True:
            p = pattern[p_index%len(pattern)]
            p_index += 1

            #VALIDATE SIDE TO SIDE MOVE
            #region
            can_move = True
            for layer in range(top_layer - SIM_CONSTANT, len(layers)):
                if layer < 0:
                    continue
                layer = layers[layer]

                for index, char in enumerate(layer):
                    if char == '@':
                        if p == '>':
                            if index == 6:
                                can_move = False
                            elif layer[index+1] == '#':
                                can_move = False
                        else:
                            if index == 0:
                                can_move = False
                            elif layer[index-1] == '#':
                                can_move = False

            if can_move:
                for layer in range(top_layer - SIM_CONSTANT, len(layers)):
                    if layer < 0:
                        continue
                    new_layer = list(' ' * 7)
                    if p == '<':
                        for index, char in enumerate(layers[layer]):
                            if char == '@':
                                new_layer[index-1] = '@'
                            elif char == '#':
                                new_layer[index] = '#'

                    else:
                        for index, char in enumerate(layers[layer][::-1]):
                            index = 6 - index
                            if char == '@':
                                new_layer[index+1] = '@'
                            elif char == '#':
                                new_layer[index] = '#'

                    layers[layer] = ''.join(new_layer)

            #endregion

            can_move_down = True
            for layer in range(top_layer - SIM_CONSTANT, len(layers)-1):
                if layer < 0:
                    continue
                for slide_index in range(0, 7):
                    if layers[layer][slide_index] == '#' and layers[layer+1][slide_index] == '@':
                        can_move_down = False

            if not can_move_down:
                for layer in range(top_layer - SIM_CONSTANT, len(layers) - 1):
                    if layer < 0:
                        continue
                    layers[layer] = layers[layer].replace('@', '#')
                break

            else:
                for layer in range(top_layer - SIM_CONSTANT, len(layers) - 1):
                    if layer < 0:
                        continue
                    for slide_index in range(0, 7):
                        if layers[layer + 1][slide_index] == '@':
                            l = list(layers[layer + 1])
                            l[slide_index] = ' '
                            layers[layer + 1] = ''.join(l)

                            l = list(layers[layer])
                            l[slide_index] = '@'
                            layers[layer] = ''.join(l)
                top_layer -= 1

            # print()
            # print(p, "+++++", p_index, len(pattern))
            # for item in layers[::-1]:
            #     print('|' + item + '|')
            # input()

    counter = 0
    for layer in layers[1:]:
        if '#' in layer:
            counter += 1
    print(counter)