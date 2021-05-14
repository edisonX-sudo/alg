import math
import random


def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot_inx = int(random.random() * len(arr))
        less = [i for inx, i in enumerate(arr) if inx != pivot_inx and i < arr[pivot_inx]]
        greater = [i for inx, i in enumerate(arr) if inx != pivot_inx and i > arr[pivot_inx]]
        return qsort(less) + [arr[pivot_inx]] + qsort(greater)


if __name__ == '__main__':
    print(qsort([92, 3, 4, 1, 6, 88, 7, 5, 6]))
