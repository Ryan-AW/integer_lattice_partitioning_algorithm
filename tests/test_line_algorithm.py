import unittest
import random
from line_algorithm import line_partition


class TestSomeFunction(unittest.TestCase):
    def test_all_small_values(self):
        for num_partitions in range(1, 101):
            for axis_len in range(num_partitions, 101):
                print(f'{axis_len=}, {num_partitions=}')
                output = line_partition(axis_len, num_partitions)
                self.assertEqual(sum(output), axis_len)

    def test_some_random_big_values(self):
        for _ in range(100):
            axis_len = random.randint(1000, 1000000)
            num_partitions = random.randint(1000, 1000000)

            if num_partitions > axis_len:
                num_partitions, axis_len = axis_len, num_partitions

            output = line_partition(axis_len, num_partitions)
            self.assertEqual(sum(output), axis_len)


if __name__ == '__main__':
    unittest.main()
