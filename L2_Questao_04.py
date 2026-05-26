from Criar_vetor import criar_vetor

v = criar_vetor(10, 1, 10)
a = []
print("V =", v)
achou = 0

for i in range(len(v)):
   achei = 0
   for j in range(len(v)):
      if(v[j] == v[i] - 1 or v[j] == v[i] + 1):
         achei = 1
   if not achei and v[i] not in a:
      achou = 1
      print("sim,", v[i],"é um elemento isolado!")
      a.append(v[i])

if not achou:
   print("Não existe no vetor!")

#Tempo de Execução = O(n^2) + O(1)*4 = O(n^2)
