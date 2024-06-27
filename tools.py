def coordinate_convert(coord_str:str) -> tuple:
    '''Transform input data from b3 to (3,3)'''
    input_transform_map = {chr(97+i):i for i in range(10)}  # dict 'a': 1, 'b': 2 etc. for transform and validate input string
    if coord_str[0] in input_transform_map.keys():
        if int(coord_str[1]) in range(10):
            return (input_transform_map[coord_str[0]], int(coord_str[1]))
    return ()

print(coordinate_convert(input("Your move: ")))
