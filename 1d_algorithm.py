def line_partition(axis_len: int, num_partitions: int):
    if num_partitions == 0:
        raise ValueError('Must have at least 1 partition.')

    if num_partitions > axis_len:
        raise ValueError("the number of partitions can't be greater than the axis length")

    partition_len, margin = divmod(axis_len, num_partitions)
    partition_len_array = [partition_len] * num_partitions

    if num_partitions % 2:
        if margin % 2:
            # set middle if both the num partitions and the grid length are odd
            partition_len_array[num_partitions//2] += 1

    if margin and num_partitions == 2:
        partition_len_array[0] += 1

    # increment from start and end of partition_len_array
    for i in range(margin//2):
        partition_len_array[i] += 1
        partition_len_array[-1 - i] += 1

    return partition_len_array


if __name__ == '__main__':
    AXIS_LEN = int(input('Enter axis length: '))
    NUM_PARTITIONS = int(input('Enter the number of partitions: '))
    print(line_partition(AXIS_LEN, NUM_PARTITIONS))
