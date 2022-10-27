def correct_name(name_info):
    if len(name_info) == 3:
        first, second, third = name_info
    elif len(name_info) == 2:
        first, second = name_info
        third = ""
    else:
        first = name_info[0]
        second, third = "", ""
    return first, second, third
