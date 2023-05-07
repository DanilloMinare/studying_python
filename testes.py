import random
#lista = ['a','b','c']
#lista2 =[]
#x = 1
#x = random.randint(0,2)
teste = [i for i in range(9)]

#ista2.append(lista.pop(x)) 
teste = {i: '{}'.format(i) for i in teste}
teste[2] = 'x'
teste[4] = 'x'
teste[6] = 'x'
teste[0] = 'x'

linha1 = {} 
linha2 = {} 
linha3 = {}  
for i in teste: 
     
    if i < 3:
        formatacao = '\33[4m'        
        linha1[i] = teste[i]
        linha1[i] = formatacao + linha1[i]        
    elif i < 6:        
        linha2[i] = teste[i]
        linha2[i] = formatacao + linha2[i] 
    elif i < 9:
         formatacao = '\33[m'
         linha3[i] = teste[i]  
         linha3[i] = formatacao + linha3[i]

print(" | ".join(str(elemento) for elemento in linha1.values()))

print(" | ".join(str(elemento) for elemento in linha2.values()))

print(" | ".join(str(elemento) for elemento in linha3.values())) 
#print(linha1)
print(type(teste[1]))



#print(lista)
#print(lista2)


