#!/usr/bin/env python
# coding: utf-8

# 1 Defina a função soma_nat que recebe como argumento um número natural n
#  e devolve a soma de todos os números naturais até n.
# 

# In[5]:


# modo nao recursivo
def soma_nat(n):
    soma=0
    for i in range(1,n+1):
        soma+=i
    return soma

print(soma_nat(5))
print(soma_nat(10))
        


# In[7]:


# modo recursivo

def soma_nat(n):
    if n==1:
        return 1
    else:
        return n + soma_nat(n-1)
    
print(soma_nat(5))
print(soma_nat(10))
        


# 2 Defina a função div que recebe como argumentos dois números naturais m e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira.

# In[ ]:


# modo procedural
def div(m,n):
    quociente=0;
    while m>=n:
        m-=n
        quociente +=1
    return quociente
print(div(10,2))
print(div(10,3)) 


# In[ ]:


# modo recursivo
def div_r(m,n):
    if m<n:
        return 0
    else:
        return 1 + div_r(m-n,n)
    
print(div_r(5,5))
print(div_r(10,3))
print(div_r(5,5))
print(div_r(10,3))


# 5 Defina a função contem_parQ que recebe como argumento uma lista de números inteiros w e devolve True se w contém um número par e False em caso contrário.

# In[ ]:


## modo procedural
def contem_parQ(w):
    for i in w:
        if i%2==0:
            return True
    else:
        return False
    
print (contem_parQ([2,3,1,2,3,4])) 
print (contem_parQ([1,3,5,7]))


# In[3]:


# modo recursivo
def r_contem_parQ(w):
    if len(w)==0:
        return False
    else:
        a=w.pop()
        if a%2==0:
            return True
        else:
            return r_contem_parQ(w)
    
print (r_contem_parQ([2,3,1,2,3,4])) 
print (r_contem_parQ([1,3,5,7]))


# In[ ]:




