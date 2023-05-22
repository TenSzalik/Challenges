def solution(args):
    range_list, temporary_range = [], []
    range_string = ""

    for value in args:
        if not temporary_range or value == temporary_range[-1] + 1:
            temporary_range.append(value)
        else:
            range_list.append(temporary_range)
            temporary_range = [value]
    range_list.append(temporary_range)

    for range in range_list:
        if len(range) < 3:
            numbers = ",".join(str(x) for x in range)
            range_string += numbers + ","
        else:
            numbers = f"{range[0]}-{range[-1]}"
            range_string += numbers + ","
    range_string = range_string[:-1]

    return range_string
