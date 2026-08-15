from Criar_vetor import criar_vetor

v = criar_vetor(10, 1, 50)
print(v)

if(v[0] > v[1]):
   m1 = v[0]; m2 = v[1]
else:
   m1 = v[1]; m2 = v[0]
if(v[2] > m1):
   m3 = m2; m2 = m1; m1 = v[2]
elif(v[2] > m2):
   m3 = m2; m2 = v[2]
else:
   m3 = v[2]

i = 3
while i < len(v):
   if(v[i] > m1):
      m3 = m2; m2 = m1; m1 = v[i]
   elif(v[i] > m2):
      m3 = m2; m2 = v[i]
   elif(v[i] > m3):
      m3 = v[i]
   i+=1

print(m3, "é o terceiro maior elemento!")

#Tempo de execução: (Vou fazer sem o criar vetor viu), O(n) + O(1)*6 = O(n)