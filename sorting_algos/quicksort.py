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

    def partition(self, arr, l, h):
        i = (l - 1)
        x = arr[h]

        for j in range(l, h):
            if arr[j] <= x:

                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                self.troca += 1
            self.comparacoes += 1

        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        self.troca += 1
        return (i + 1)

    def quickSortIterative(self, arr, l, h):

        start_time = time.time()

        size = h - l + 1
        stack = [0] * (size)

        top = -1

        top = top + 1
        stack[top] = l
        top = top + 1
        stack[top] = h

        while top >= 0:

            h = stack[top]
            top = top - 1
            l = stack[top]
            top = top - 1

            p = self.partition(arr, l, h)

            if p - 1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1
                self.comparacoes += 1

            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h
                self.comparacoes += 1

        execution_time = time.time() - start_time

        return stack, {
            "time": execution_time,
            "comparacoes": self.comparacoes,
            "troca": self.troca
        }
