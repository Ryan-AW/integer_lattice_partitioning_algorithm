from colorsys import hsv_to_rgb


def generate_colors(num_colors: int):
    for i in range(num_colors):
        yield hsv_to_rgb(i*(1.0/num_colors), 1.0, 1.0)
