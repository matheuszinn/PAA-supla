import time


class CombSort:
    def __init__(self):
        self.comparacoes = 0
        self.troca = 0

    def combsort(self, A):
        tempo = time.time()

        gap = len(A)
        ativo = True

        while gap != 1 or ativo:
            gap = max(1, int(gap / 1.13))
            ativo = False
            for i in range(len(A) - gap):
                j = i + gap
                if A[i] > A[j]:
                    self.comparacoes += 1
                    A[j], A[i] = A[i], A[j]
                    self.trocas += 1
                    ativo = True

        tempo_de_execucao = time.time() - tempo

        return A, {
                "time": tempo_de_execucao,
                "comparacoes": self.comparacoes,
                "troca": self.troca,
            }