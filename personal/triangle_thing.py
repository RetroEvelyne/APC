def layer(length: int) -> str:
    return_str = ""
    for i in range(length):
        if (i % 2) == 0:
            return_str += "*"
        else:
            return_str += "A"
    return return_str

def pyramid(height:int) -> str:
    pyramid_str = ""
    buffer = " "*(height-1)
    last_length = 1

    for _ in range(height):
        pyramid_str += buffer
        buffer = buffer[:-1]
        pyramid_str += layer(last_length)
        last_length += 2
        pyramid_str += "\n"

    return pyramid_str

