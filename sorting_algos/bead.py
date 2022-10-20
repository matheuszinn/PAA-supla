import copy as copy
import random
import time
import sys


class BeadSort:
    def __init__(self) -> None:
        self.comparacoes = 0
        self.troca = 0

    def bead_sort(self, list):
        start_time = time.time()
        if all([type(x) == int and x >= 0 for x in list]):
            ref = [range(x) for x in list]  # for reference
        else:
            raise ValueError("All elements must be positive integers")

        inter = []  # for intermediate
        ind = 0  # for index
        prev = sum([1 for x in ref if len(x) > ind])
        self.comparacoes += len(ref)  # prev for previous
        while prev:
            inter.append(range(prev))
            ind += 1
            prev = sum([1 for x in ref if len(x) > ind])
            self.comparacoes += len(ref)  # prev for previous
        ind = 0
        prev = sum([1 for x in inter if len(x) > ind])
        self.comparacoes += len(inter)  # prev for previous
        out = []
        while prev:
            out.append(prev)
            ind += 1
            prev = sum([1 for x in inter if len(x) > ind])
            self.comparacoes += len(inter)  # prev for previous
        out = out[::-1]
        execution_time = time.time() - start_time
        return out, {
            "time": execution_time,
            "comparacoes": self.comparacoes,
            "troca": self.troca,
        }
