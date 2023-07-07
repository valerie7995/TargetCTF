#!/usr/bin/env python
from PIL import Image
import ctypes
width = 4096
height = 4096
img = Image.new("RGB", (width, height))
red = (0, 0, 0)  # Skipping Right Mouse Btn, it's not needed at all
green = (0, 255, 0)
blue = (0, 0, 255)
default = (0, 0, 0)
colormap = {
    0: red,
    1: green,
    2: blue
}
x = width // 2
y = height // 2
with open('mouse_clickss.txt') as f:
    for line in f:
        bytes = list(map(lambda v: int('0x'+v, 16), line.split(":")))
        b0, b1, b2, b3 = bytes
        # byte0: 0==LBM, 1=RBM, 2=MBM
        color = colormap.get(b0, default)
        # byte1: X displacement
        x_dis = ctypes.c_int8(b1).value
        # byte2: Y displacement
        y_dis = ctypes.c_int8(b2).value
        x = max(0, min(x + x_dis, width - 1))
        y = max(0, min(y + y_dis, height - 1))
        img.putpixel((x, y), color)
img.save("image.png")
