def build_slice(width, side_left, side_right, inside):
    slice=str(side_left)
    for i in range(0, int(width-2)):
        slice = slice + str(inside)
    slice = slice + str(side_right)
    return slice