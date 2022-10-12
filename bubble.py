
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

#função de busca
def bubble_sort(list):

    
    old_list = copy.deepcopy(list) #lista antiga
    num_trocas = 0 #armazena a quantidade de trocas realizadas
    num_comp = 0 #armazena a quantidade de comparações realizadas
    
    #actual sorting
    while True:
        did_swap = False
        for index, value in enumerate(list):

            if (index != len(list)-1) and ((value) > list[index+1]):
                list[index] = list[index+1] #trocas 
                list[index+1] = value       
                num_trocas = num_trocas + 1 #stats
                if did_swap != True:
                    did_swap = True
            num_comp = num_comp + 1 #stats
        if did_swap == False:
            break

    #impressão das estatísticas
    #print(old_list) lista antiga para testes
    print(list)#lista atual. NÁO IMPRIMA AS LISTAS PARA TAMANHOS MUITO GRANDES
    print("trocas: {} \ncomparações: {}".format(num_trocas, num_comp))


if __name__ == '__main__':
    start_time = time.time()  # salva o tempo atual para calculo do tempo de execução
    print('tempo iniciado')

    list = generate_list(100)
    bubble_sort(list)

    # realiza o calculo do tempo percorrido
    execution_time = time.time() - start_time

    #imprime outras estatísticas
    print("tempo: {}".format(execution_time))
    print("tamanho: {} bytes".format(sys.getsizeof(list)))
    print('feito!')
