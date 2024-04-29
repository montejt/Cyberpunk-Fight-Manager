def calc_max_pixel_width(strings):
    max_len = 0
    for string in strings:
        max_len = max(max_len, len(string))
    
    return max_len
