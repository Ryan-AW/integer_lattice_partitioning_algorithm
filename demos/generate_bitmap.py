from colorsys import hsv_to_rgb
from algorithms.plane_algorithm import plane_partition


def generate_colors(num_colors: int):
    for i in range(num_colors):
        yield hsv_to_rgb(i*(1.0/num_colors), 1.0, 1.0)


def transform(plane_xy: tuple[int, int], num_columns: int, num_rows: int):
    partition = plane_partition(plane_xy, num_columns, num_rows)
    color_array = list(generate_colors(len(partition['horizontal'])*len(partition['vertical'])))

    bitmap = []
    for i, num_repeats in enumerate(partition['vertical']):
        row = []
        for j, seg_length in enumerate(partition['horizontal']):
            row += [color_array[(i*num_rows)+j]] * seg_length

        for _ in range(num_repeats):
            bitmap.append(row)
    return bitmap
