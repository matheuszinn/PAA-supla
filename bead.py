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


def bead_sort(list):
  if all([type(x) == int and x >= 0 for x in list]):
    ref = [range(x) for x in list]  #for reference
  else:
    raise ValueError("All elements must be positive integers")
    
  inter = []  #for intermediate
  ind = 0  #for index
  prev = sum([1 for x in ref if len(x) > ind])  #prev for previous
  while prev:
      inter.append(range(prev))
      ind += 1
      prev = sum([1 for x in ref if len(x) > ind])
  ind = 0
  prev = sum([1 for x in inter if len(x) > ind])
  out = []
  while prev:
      out.append(prev)
      ind += 1
      prev = sum([1 for x in inter if len(x) > ind])
  out = out[::-1]
  return out

if __name__ == '__main__':
    start_time = time.time()  # salva o tempo atual para calculo do tempo de execução
    print('tempo iniciado')

    list = generate_list(100)
    bead_sort(list)

    # realiza o calculo do tempo percorrido
    execution_time = time.time() - start_time

    #imprime outras estatísticas
    print("tempo: {}".format(execution_time))
    print("tamanho: {} bytes".format(sys.getsizeof(list)))
    print('feito!')