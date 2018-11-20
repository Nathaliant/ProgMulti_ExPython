#!/usr/bin/env python
# coding: utf-8

# ## Exercicio 13
# Aluno: Nathalia Nogueira Torres RA:816114445

# #### 1 Defina a função soma_nat que recebe como argumento um número natural n e devolve a soma de todos os números naturais até n.

# In[7]:


soma = lambda n: n+n-1 if n==1 else n+soma(n-1)


# In[10]:


print(soma(5))
print(soma(10))


# #### 2 Defina a função div que recebe como argumentos dois números naturais m e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira.

# In[20]:


l_div = lambda m,n: 0 if m<n else 1+l_div(m-n,n)


print(l_div(5,5))
print(l_div(10,3))
print(l_div(5,5))
print(l_div(10,3))


# #### 5 Defina a função contem_parQ que recebe como argumento uma lista de números inteiros w e devolve True se w contém um número par e False em caso contrário.

# In[1]:


l_contem_parQ= lambda w: False if len(w)==0 else True if w.pop()%2==0 else l_contem_parQ(w)

print (l_contem_parQ([2,3,1,2,3,4])) 
print (l_contem_parQ([1,3,5,7]))


# In[3]:





# In[ ]:




