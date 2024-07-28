AXIS_LEN = int(input('Enter axis length: '))
NUM_PARTITIONS = int(input('Enter the number of partitions: '))

if NUM_PARTITIONS > AXIS_LEN:
    raise ValueError("the number of partitions can't be greater than the axis length")

partition_len, margin = divmod(AXIS_LEN, NUM_PARTITIONS)
partition_len_array = [partition_len] * NUM_PARTITIONS


if NUM_PARTITIONS % 2:
    if margin % 2:
        partition_len_array[NUM_PARTITIONS//2] += 1  # set middle if both the num partitions and the grid length are odd

if margin and NUM_PARTITIONS == 2:
    partition_len_array[0] += 1

# increment from start and end of partition_len_array
for i in range(margin//2):
    partition_len_array[i] += 1
    partition_len_array[-1 - i] += 1

print(partition_len_array)
