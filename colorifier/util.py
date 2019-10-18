import math


def hex2rgb(hex):
    hex = hex.strip("#")
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def hsv2rgb(hsv):
    h, s, v = hsv
    i = math.floor(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    r, g, b = [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    ][int(i % 6)]

    return r, g, b
