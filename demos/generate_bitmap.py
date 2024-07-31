from PIL import Image
from colorsys import hsv_to_rgb
from algorithms.plane_algorithm import plane_partition


def generate_colors(num_colors: int):
    for i in range(num_colors):
        yield hsv_to_rgb(i*(1.0/num_colors), 1.0, 1.0)


def generate_bitmap(filename: str, plane_xy: tuple[int, int], num_columns: int, num_rows: int):
    partition = plane_partition(plane_xy, num_columns, num_rows)
    width, height = sum(partition['horizontal']), sum(partition['vertical'])

    color_array = list(generate_colors(len(partition['horizontal'])*len(partition['vertical'])))

    bitmap = []
    for i, num_repeats in enumerate(partition['vertical']):
        row = []
        for j, seg_length in enumerate(partition['horizontal']):
            row += [color_array[(i*len(partition['horizontal']))+j]] * seg_length

        for _ in range(num_repeats):
            bitmap.append(row)

    img = Image.new('RGB', (width, height))
    pixels = img.load()
    for y in range(height):
        for x in range(width):
            pixels[x, y] = (
                int(bitmap[y][x][0] * 255),
                int(bitmap[y][x][1] * 255),
                int(bitmap[y][x][2] * 255)
            )
    img.save(filename+'.bmp', 'BMP')


generate_bitmap(
            filename=input('Enter Filename For The Output: '),
            plane_xy=(
                int(input('Enter plane width: ')),
                int(input('Enter plane height: '))
            ),

            num_columns=int(input('Enter number of columns: ')),
            num_rows=int(input('Enter number of rows: '))
        )