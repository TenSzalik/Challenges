import copy

def add_and_pop_to_snail(snail_map, sorted_list):
    sorted_list.append(snail_map[0])
    snail_map.pop(0)

def get_rotated_list(snail_map):
    rotated_list = []
    new_snail_map = copy.deepcopy(snail_map)
    count = range(len(new_snail_map[0]))

    for j in count:
        lvl_of_snail = []
        for x in new_snail_map:
            lvl_of_snail.append(x[-1])
            x.pop(-1)
        rotated_list.append(lvl_of_snail)

    return rotated_list

def snail(snail_map):
    sorted_list = []
    count = len([item for sublist in snail_map for item in sublist])
    
    if count <= 1:
        return snail_map[0]

    add_and_pop_to_snail(snail_map, sorted_list)
    while count != len([item for sublist in sorted_list for item in sublist]):
        snail_map = get_rotated_list(snail_map)
        add_and_pop_to_snail(snail_map, sorted_list)

    return [item for sublist in sorted_list for item in sublist]
