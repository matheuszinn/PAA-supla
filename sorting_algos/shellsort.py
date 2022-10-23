import time


class Shellsort:

    def __init__(self):
        self.troca = 0
        self.comparacao = 0

    def shellsort(self, array):

        start_time = time.time()

        n = len(array)
        
        # Rearrange elements at each n/2, n/4, n/8, ... intervals
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
    
                array[j] = temp
            interval //= 2
    
            execution_time = time.time() - start_time

        return array, {
            "time": execution_time,
            "comparacoes": self.comparacao,
            "troca": self.troca
        }


import random

print(Shellsort().shellsort([random.randint(1, 10000)
                             for _ in range(10)])[0])
