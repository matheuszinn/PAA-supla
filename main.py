from sorting_algos import Quicksort

import random

if __name__ == '__main__':
    l = [i for i in range(1, 1000000)]
    random.shuffle(l)
    print(Quicksort().quicksort(l, 0, len(l) - 1)[1])