import time


class InsertionSort:

    def __init__(self) -> None:
        self.comparacoes = 0
        self.troca = 0

    def insertion_sort(self, list):
        start_time = time.time()

        for p in range(1, len(list)):
            aux = list[p]

            q = p - 1
            self.comparacoes = self.comparacoes + 1

            while q >= 0 and aux < list[q]:
                self.comparacoes = self.comparacoes + 1
                list[q + 1] = list[q]
                q = q - 1
                self.troca = self.troca + 1
            list[q + 1] = aux

        execution_time = time.time() - start_time
        return list, {
            "time": execution_time,
            "comparacoes": self.comparacoes,
            "troca": self.troca,
        }
