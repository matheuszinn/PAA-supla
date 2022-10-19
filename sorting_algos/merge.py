import time
from sorting_algos.helpers import infos_algoritmos


class Mergesort:

    def __init__(self):
        self.comparacoes = 0
        self.trocas = 0

    def merge_sort(self, arr: list[int]) -> tuple[
        list[int], dict[str, int | float]]:
        start_time = time.time()
        r = self.__top_down(arr)
        execution_time = time.time() - start_time
        return r, infos_algoritmos(tempo=execution_time,
                                   comparacoes=self.comparacoes,
                                   trocas=self.trocas)

    def __merge(self, _esq: list[int], _dir: list[int]) -> list[int]:
        result: list[int] = []

        while len(_esq) != 0 and len(_dir) != 0:
            if _esq[0] <= _dir[0]:
                result.append(_esq.pop(0))
            else:
                result.append(_dir.pop(0))
            self.comparacoes += 1

        while len(_esq) != 0:
            result.append(_esq.pop(0))

        while len(_dir) != 0:
            result.append(_dir.pop(0))

        return result

    def __top_down(self, arr: list[int]):

        if len(arr) <= 1:
            return arr

        _dir: list[int] = []
        _esq: list[int] = []

        for idx, item in enumerate(arr):
            if idx < len(arr) / 2:
                _esq.append(item)
            else:
                _dir.append(item)

        _esq = self.__top_down(_esq)
        _dir = self.__top_down(_dir)

        return self.__merge(_esq, _dir)
