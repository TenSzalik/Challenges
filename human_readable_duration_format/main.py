TIME_FORMAT = [
      ("year", 60 * 60 * 24 * 365),
      ("day", 60 * 60 * 24),
      ("hour", 60 * 60),
      ("minute", 60),
      ("second", 1),
]

def format_duration(raw_seconds: int) -> str:
    if not raw_seconds:
            return "now"
    
    seconds_in_list_of_tuple_format = []

    for name, named_seconds in TIME_FORMAT:
        seconds_sumed_as_name = raw_seconds // named_seconds

        if seconds_sumed_as_name is 1:
            seconds_in_list_of_tuple_format.append((seconds_sumed_as_name, name))
            raw_seconds -= named_seconds
        elif seconds_sumed_as_name > 1:
            seconds_in_list_of_tuple_format.append((seconds_sumed_as_name, name+"s"))
            raw_seconds -= named_seconds * seconds_sumed_as_name

    string_format_without_and = ", ".join([f"{x} {y}" for x,y in seconds_in_list_of_tuple_format])
    string_format = string_format_without_and[::-1].replace(",", "dna ", 1)[::-1]

    return string_format