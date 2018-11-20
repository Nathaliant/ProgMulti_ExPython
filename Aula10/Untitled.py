#!/usr/bin/env python
# coding: utf-8

# #### 1. Faça um Programa que peça dois números e imprima o maior deles

# In[ ]:


x1 = int(input('Digite o primeiro número: '))
x2 = int(input('Digite o segundo número: '))
print("o maior número é", max(x1,x2))

if x>y:
    print(f'{x1} é maior que {x2}')
elif x<y:
    print(f'{x2} é maior que {x1}')   
else: 
    print(f'{x1} é igual a {x2}')


# #### 4. Faça um Programa que leia três números e mostre-os em ordem decrescente

# In[6]:


entrada=[(1,2,3,), (1,3,2,), (2,1,3,), (2,3,1), (3,2,1,), (3,1,2)]

for x,y,z in entrada:
    if x>y:
        if y>z:
            print(x,y,z)
        else:
            if x>z:
                print(x,z,y)
            else:
                print(z,x,y)
    else:
        #y>x
        if y>z:
            if x>z:
                print(y,x,z)
            else:
                print(y,z,x)
        else:
            #y>x e z>y
            print(z,y,x)


# 19. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
# 

# In[1]:


n=10
numero=n
fatorial=1
while n>0:
    fatorial*=n
    n-=1
print(f'{numero}!={fatorial}')
    


# 25. Faça um programa que mostre os n termos da Série a seguir:
#  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

# In[4]:


n=30
x=1
y=1
soma=0
while x<=n:
    soma+=(x/y)
    x+=1
    y+=2
print(soma)
    
    


# In[ ]:




