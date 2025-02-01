def ishex(color, alpha=False):
    if not color or not color[0] == "#":
        return False

    color = color[1:]

    allowed = (3, 6)
    if alpha:
        allowed += (4, 8)

    if len(color) not in allowed:
        return False

    try:
        int(color, 16)
        return True
    except ValueError:
        return False


def normhex(color, alpha=False):
    if color and not color[0] == "#":
        color = "#" + color

    if not ishex(color, alpha):
        return None

    color = color[1:]
    size = len(color)

    allowed = (6,)
    if alpha:
        allowed += (8,)

    if size in allowed:
        return "#" + color

    allowed = (3,)
    if alpha:
        allowed += (4,)

    if size in allowed:
        return '#' + "".join(c + c for c in color)
    return None


def rgba2hex(red, green, blue, alpha=1.0):
    try:
        values = list(min(max(c, 0), 255) for c in (red, green, blue))
        values.append(255 * alpha)
        return '#{:02x}{:02x}{:02x}{:02x}'.format(*values)
    except (TypeError, ValueError):
        return None


def rgb2hex(red, green, blue):
    return rgba2hex(red, green, blue, 0)[:-2]


def hex2rgba(color):
    color = normhex(color, True)
    if not color:
        return None
    color = color[1:]
    try:
        return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4, 6))
    except (TypeError, ValueError):
        return None


def hex2rgb(color):
    return hex2rgba(color)[:-1]
