AXIS_LEN = 10

PARTITION_LEN = 3
NUM_PARTITIONS = 3

partition_len_array = [PARTITION_LEN] * NUM_PARTITIONS


if AXIS_LEN % 2:
    if NUM_PARTITIONS % 2:
        partition_len_array[NUM_PARTITIONS//2] += 1  # set middle if both the num partitions and the grid length are odd
