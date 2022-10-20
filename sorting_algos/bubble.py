import copy as copy
import time

class BubbleSort:
    def __init__(self) -> None:
        self.comparacoes = 0
        self.troca = 0

    # função de busca
    def bubble_sort(self, list):

        old_list = copy.deepcopy(list)  # lista antiga
        num_trocas = 0  # armazena a quantidade de trocas realizadas
        num_comp = 0  # armazena a quantidade de comparações realizadas

        start_time = time.time()

        # actual sorting
        while True:
            did_swap = False
            for index, value in enumerate(list):

                if (index != len(list) - 1) and ((value) > list[index + 1]):
                    list[index] = list[index + 1]  # trocas
                    list[index + 1] = value
                    self.troca = self.troca + 1  # stats
                    if did_swap != True:
                        did_swap = True
                self.comparacoes = self.comparacoes + 1  # stats
            if did_swap == False:
                break
        execution_time = time.time() - start_time

        return list, {
            "time": execution_time,
            "comparacoes": self.comparacoes,
            "troca": self.troca,
        }
