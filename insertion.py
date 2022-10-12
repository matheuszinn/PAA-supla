
import copy as copy
import random
import time
import sys

random.seed(69420)

# gera uma lista de tamanho "size" (10, 100, 1000, 10000, 20000, 30000,..., 1000000000)


def generate_list(size):

    list = []
    for p in range(size):
        list.append(random.randint(1, 1000))
    return list

def insertion_sort(list):
    old_list = copy.deepcopy(list)
    num_trocas = 0
    num_comp = 0

    for p in range(1, len(list)):
        aux = list[p]
        
        q = p-1
        num_comp = num_comp+1

        while q >=0 and aux < list[q]:
            num_comp=num_comp+1
            list[q+1] = list[q]
            q = q-1
            num_trocas = num_trocas+1
        list[q+1] = aux

    print(old_list)
    print(list)
    print("trocas: {} \ncomparações: {}".format(num_trocas, num_comp))

'''
def insertion_sort(list):
    old_list = copy.deepcopy(list)
    num_trocas = 0
    num_comp = 0

    # Traverse through 1 to len(arr)
    for p in range(1, len(list)):
  
        aux = list[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        q = p-1
        num_comp+=1
        while q >= 0 and aux < list[q] :
            num_comp = num_comp + 1
                list[q + 1] = list[q]
                q = q - 1
                num_trocas = num_trocas + 1
        list[q + 1] = aux
        
    
    print(old_list)
    print(list)
    print("trocas: {} \ncomparações: {}".format(num_trocas, num_comp))
  '''


if __name__ == '__main__':
    start_time = time.time()  # salva o tempo atual para calculo do tempo de execução
    print('tempo iniciado')

    list = generate_list(80000)
    insertion_sort(list)

    # realiza o calculo do tempo percorrido
    execution_time = time.time() - start_time

    print("tempo: {}".format(execution_time))
    print("tamanho: {} bytes".format(sys.getsizeof(list)))
    print('feito!')


