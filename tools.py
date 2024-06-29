def coordinate_convert(coord_str: str) -> tuple:
    '''Transform input data from b3 to (1,2)'''

    # dict 'a': 1, 'b': 2 etc. for transform and validate input string
    input_transform_map = {chr(97+i): i for i in range(10)}
    if coord_str[0] in input_transform_map.keys():
        if int(coord_str[1:]) in range(1, 11):
            return (input_transform_map[coord_str[0]], int(coord_str[1:]) - 1)
    return ()


if __name__ == "__main__":  
    # print(coordinate_convert(input("Your move: ")))

    ship = [(0,5), (0,6), (0,7)]
    for deck in ship:
        r, c = deck
        print(r, c)

