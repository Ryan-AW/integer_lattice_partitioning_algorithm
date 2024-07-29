from line_algorithm import line_partition


def plane_partition(plane_xy: tuple[int, int], num_columns: int, num_rows: int):
    return {'horizontal': line_partition(plane_xy[0], num_columns),
            'vertical': line_partition(plane_xy[1], num_rows)}
