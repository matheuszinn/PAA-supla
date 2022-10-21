import copy as copy
import math
import time
from random import shuffle
from typing import List
from random import randrange


class Quicksort:
    def __init__(self):
        self.comparacoes = 0
        self.troca = 0

    def quicksort(self, A, low=0, high=None):
        start_time = time.time()
        high = high if high is not None else len(A)
        if low < high:
            part = self.particao(A, low, high)
            self.quicksort(A, low, part)
            self.quicksort(A, part + 1, high)
            self.comparacoes += 1

        execution_time = time.time() - start_time
        return A, {
            "time": execution_time,
            "comparacoes": self.comparacoes,
            "troca": self.troca,
        }

    def particao(self, A, low, high):
        r = randrange(low, high)
        A[r], A[low - 1] = A[low - 1], A[r]
        self.troca += 1
        pivo = A[high - 1]
        for i in range(low, high):
            if A[i] > pivo:
                high += 1
            else:
                high += 1
                low += 1
                A[i], A[low - 1] = A[low - 1], A[i]
                self.troca += 1
            self.comparacoes += 1
        return low - 1

import random
print(Quicksort().quicksort([random.randint(1,1000) for _ in range(1000)])[1])