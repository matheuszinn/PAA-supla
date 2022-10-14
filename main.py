from sorting_algos import Mergesort

import random

if __name__ == '__main__':
    l = [i for i in range(1, 1000)]
    random.shuffle(l)
    print(Mergesort().merge_sort(l)[1])