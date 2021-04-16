import utils

def rectangle(width, height):
    slice_out = utils.build_slice(width, "|", "|", "-")
    slice_in = utils.build_slice(width, "|", "|", " ")
    print(slice_out)
    for i in range(0, height-2):
        print(slice_in)
    print(slice_out)

rectangle(20,10)