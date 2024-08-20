# # Speed up CPU bound program
# import multiprocessing
# import time

# def sum_func(number):
#     _sum = 0
#     # print(number)
#     for i in range(number):
#         _sum += i
#     print(f'[SUM]: {_sum}')
#     return _sum
 
# def find_sum(numbers):
#     with multiprocessing.Pool() as pool:
#         # print(sum_func)
#         pool.map(sum_func, numbers)

# if __name__ == "__main__":
#     numbers = [5000000]*3
#     # print(numbers)
#     start_time = time.time()
#     find_sum(numbers)
#     print(f'[MAIN] [FINISHED]: {time.time() - start_time}')

# import unittest

# def sum_func(a, b):
#     return a + b

# class FuncTestCase(unittest.TestCase):
#     def test_sum_func(self):
#         a = [1, 2, 3]
#         b = [1, 2, 3]
#         c = [2, 4, 6]
#         # print(zip(a, b, c))
#         for _a, _b, _c in zip(a, b, c):
#             with self.subTest():
#                 self.assertEqual(sum_func(_a, _b), _c)
#         # self.assertEqual(1, 1)


# if __name__ == "__main__":
#     unittest.main()

