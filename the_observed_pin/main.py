def generate_numbers(possible: list):
    def inner(current_index, current_number):
        if current_index == len(possible):
            result.append(current_number)
            return None

        for digit in possible[current_index]:
            new_number = current_number + str(digit)
            inner(current_index + 1, new_number)

    result = []
    inner(0, "")
    return result


def get_pins(observed: str):
    pins_schema = (
        (0, 8),
        (1, 2, 4),
        (2, 1, 3, 5),
        (3, 2, 6),
        (4, 1, 5, 7),
        (5, 2, 4, 6, 8),
        (6, 3, 5, 9),
        (7, 4, 8),
        (8, 5, 7, 9, 0),
        (9, 6, 8),
    )
    possible = [pins_schema[int(n)] for n in observed]
    return generate_numbers(possible)
