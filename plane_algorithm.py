from line_algorithm import line_partition


def plane_partition(plane_xy: tuple[int, int], num_columns: int, num_rows: int):
    return {'horizontal': line_partition(plane_xy[0], num_columns),
            'vertical': line_partition(plane_xy[1], num_rows)}


if __name__ == '__main__':
    print(
        plane_partition(
            plane_xy=(
                int(input('Enter plane width: ')),
                int(input('Enter plane height: '))
            ),

            num_columns=int(input('Enter number of columns: ')),
            num_rows=int(input('Enter number of rows: '))
        )
    )
