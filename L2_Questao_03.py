from Criar_vetor import criar_vetor

v = criar_vetor(10, 1, 20)
print("V =", v)
soma = 0; i = 0

while i < len(v):
   soma += v[i]
   i+=1

media = soma/len(v)
dif = abs(media - v[0])
prox = v[1]
j = 1

while j < len(v):
   teste = abs(media - v[j])
   if(teste < dif):
      dif = teste
      prox = v[j]
   j+=1

print(prox,"é o número mais próximo da média", media)

#Tempo de execução = O(n) + O(n) + O(1)*7 = 2*O(n) = O(n)