import utils

def draw_triangle(height):
    for i in range(1, height):
        spaces = "".join([' '] * (height-i))
        print(str(spaces) + str(utils.build_slice(2*i, "/", "\\", " ")))
    print(utils.build_slice(2*(height), "/", "\\", "_"))


draw_triangle(10)