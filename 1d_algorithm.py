AXIS_LEN = 10

NUM_PARTITIONS = 3

partition_len, margin = divmod(AXIS_LEN, NUM_PARTITIONS)
partition_len_array = [partition_len] * NUM_PARTITIONS


if NUM_PARTITIONS % 2:
    if margin % 2:
        partition_len_array[NUM_PARTITIONS//2] += 1  # set middle if both the num partitions and the grid length are odd

# increment from start and end of partition_len_array
for i in range(margin//2):
    partition_len_array[i] += 1
    partition_len_array[-1 - i] += 1
