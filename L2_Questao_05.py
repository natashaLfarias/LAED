import random
from Criar_vetor import criar_vetor

v = criar_vetor(10, 1, 10)
k = random.randint(1, 5)

print("V =", v, "K =", k)
a =[]

achei = 0
for i in range(len(v)):
   cont = 1
   for j in range(i+1,len(v), 1):
      if(v[j] == v[i]):
         cont+=1
        
   if(cont >= k and v[i] not in a): #pelo menos k vezes
      achei = 1
      a.append(v[i])
      print("Sim, o",v[i],"se repete pelo menos",k,"vezes!")

if not achei:
   print("Não tem!")

#Tempo de Execução = O(n^2) + O(1)*3 = O(n^2)