import random
from random import randint
def criar_vetor(n, lim_i, lim_f):
  vetor = [0] * n
  for i in range(n):
      vetor[i] = random.randint(lim_i, lim_f)

  return vetor