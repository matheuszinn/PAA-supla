import copy as copy
import math
import time
from random import shuffle
from typing import List


class Quicksort:

    def __init__(self):
        self.comparacoes = 0
        self.troca = 0

    def quicksort(self, A, low=0, high=None):
        start_time = time.time()
        if low < high:
            part = self.particao(A, low, high)
            self.quicksort(A, low, part - 1)
            self.quicksort(A, part + 1, high)
            self.comparacoes += 1

        execution_time = time.time() - start_time
        return A, {"time": execution_time, "comparacoes": self.comparacoes, "troca": self.troca}

    def particao(self, A, low, high):
        pivot = A[high]
        i = low - 1

        for j in range(low, high):
            if A[j] <= pivot:
                i = i + 1
                (A[i], A[j]) = (A[j], A[i])
                self.comparacoes += 1
            self.troca += 1

        (A[i + 1], A[high]) = (A[high], A[i + 1])
        self.comparacoes += 1
        return i + 1
