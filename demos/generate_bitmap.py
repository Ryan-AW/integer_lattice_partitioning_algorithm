from PIL import Image
from colorsys import hsv_to_rgb
from random import sample
from algorithms.plane_algorithm import plane_partition


def generate_colors(num_colors: int):
    return sample([hsv_to_rgb(i*(1.0/num_colors), 1.0, 1.0) for i in range(num_colors)], num_colors)


def generate_bitmap(filename: str, plane_xy: tuple[int, int], num_columns: int, num_rows: int):
    partition = plane_partition(plane_xy, num_columns, num_rows)

    print()
    print(partition)
    print()

    width, height = sum(partition['horizontal']), sum(partition['vertical'])

    color_array = generate_colors(len(partition['horizontal'])*len(partition['vertical']))

    bitmap = []
    for i, num_repeats in enumerate(partition['vertical']):
        row = []
        for j, seg_length in enumerate(partition['horizontal']):
            row += [color_array[(i*len(partition['horizontal']))+j]] * seg_length

        for _ in range(num_repeats):
            bitmap.append(row)

    img = Image.new('RGB', (width, height))
    pixels = img.load()

    try:
        from tqdm import tqdm

        for y in tqdm(range(height), desc="rows complete"):
            for x in range(width):
                pixels[x, y] = (
                    int(bitmap[y][x][0] * 255),
                    int(bitmap[y][x][1] * 255),
                    int(bitmap[y][x][2] * 255)
                )
    except ImportError:
        print('tip: install the python "tqdm" module for a progress bar!')
        print()
        print('GENERATING BITMAP...', end='')

        for y in range(height):
            for x in range(width):
                pixels[x, y] = (
                    int(bitmap[y][x][0] * 255),
                    int(bitmap[y][x][1] * 255),
                    int(bitmap[y][x][2] * 255)
                )

        print(' done!')
        print()
    img.save(filename+'.bmp', 'BMP')

    print(f'SAVED AS "{filename}.bmp"')


generate_bitmap(
            filename=input('Enter Filename For The Output: '),
            plane_xy=(
                int(input('Enter plane width: ')),
                int(input('Enter plane height: '))
            ),

            num_columns=int(input('Enter number of columns: ')),
            num_rows=int(input('Enter number of rows: '))
        )
