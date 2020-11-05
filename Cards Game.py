#!/usr/bin/env python
# coding: utf-8

# #  start from here

# In[242]:


cards=["A of Clubs","2 of Clubs","3 of Clubs","4 of Clubs","5 of Clubs","6 of Clubs","7 of Clubs","8 of Clubs","9 of Clubs","10 of Clubs"
      ,"A of Diamonds","2 of Diamonds","3 of Diamonds","4 of Diamonds","5 of Diamonds","6 of Diamonds","7 of Diamonds","8 of Diamonds","9 of Diamonds","10 of Diamonds"
      ,"A of Hearts","2 of Hearts","3 of Hearts","4 of Hearts","5 of Hearts","6 of Hearts","7 of Hearts","8 of Hearts","9 of Hearts","10 of Hearts"
      ,"A of Spades","2 of Spades","3 of Spades","4 of Spades","5 of Spades","6 of Spades","7 of Spades","8 of Spades","9 of Spades","10 of Spades"
      ,"Jack of Clubs","Jack of Diamonds","Jack of Hearts","Jack of Spades"
      ,"Queen of Clubs","Queen of Diamonds","Queen of Hearts","Queen of Spades"
      ,"King of Clubs","King of Diamonds","King of Hearts","King of Spades"
      ]

cards_prio={'Clubs': 5, 
            'Diamonds': 5, 
            'Hearts': 5, 
            'Spades': 5 ,
            'Jack': 4,
            'Queen': 3 ,
            'King': 2 ,
            'A': 1
           }


# In[243]:


import random


# In[244]:


random.shuffle(cards)


# In[245]:


print(cards)


# In[246]:


c1=cards[:26]
c2=cards[26:]


# In[247]:


print(c1,len(c1))


# In[248]:


print(c2,len(c2))


# In[236]:


# challenge function
# c1 - Donald(cards)  c2- joe(cards)
def drow(c1, c2):
    print("drow1")
    li=[]
    if len(c1)>4:
        for i in range(0,4,1):
            li.append(c1.pop(i))
        print(print("-**"),li)
    else:
        joe["Challenges"]+=1
    if len(c2)>4:
        for i in range(0,4,1):
            li.append(c2(i))
        print(print("-***"),li)
    else:
        Donald["Challenges"]+=1
    return li
        
    
# Main function 
# 1st play by donald by default 
# t1, t2 - card1 and card2 of c1 and c2
def match(c1, c2):
    t1 = c1[0].split(" ") 
    t2 = c2[0].split(" ")
    print(len(c1),len(c2))
    c1.remove(c1[0])
    c2.remove(c2[0])
    print(len(c1),len(c2))
    print(t1)
    print(t2)
    
    # j1- donald card rank  j2-joe card rank
    j1 = 0
    j2 = 0
    
    #aa- donald flag(number-0 or spl card-1)  
    #bb- joe flag(number-0 or spl card-1)
    aa = 0
    bb = 0
    
    #w1- donald flag for winner
    #w2- joe flag for wimmer
    w1 = 0
    w2 = 0
    
    #draw container for 8 cards appending
    li = 0
    
    if (t1[0].isdigit()):
        aa=0
        j1=int(t1[0])
    else:
        aa=1
        j1=cards_prio[t1[0]] #2
    
    if (t2[0].isdigit()):
        bb=0
        j1=int(t2[0])
    else:
        bb=1
        j1=cards_prio[t2[0]] #'jack'
        
    if (aa==0) and (bb==0) or (aa==1) and (bb==1):
        if j1 < j2:
            print("**")
            Donald['Tricks']+=1
            w1 = 1
        elif j1 > j2:
            print("***")
            w2 = 1 
            joe['Tricks']+=1
        else:
            print("****")
            li=drow(c1,c2) 
            match(li[-2], li[-1])
            
            
    elif (aa==0) and (bb==1):
        if j1 == 1 and j2 == 2:
            w1 = 1
            Donald['Tricks']+=1
            Donald['Aces']+=1
        elif j1 ==2 and j2 == 1:
            w2 = 1
            joe['Tricks']+=1
            joe['Aces']+=1
        else:
            w2 = 1
            joe['Tricks']+=1
            
    elif (aa==1) and (bb==0):
        print("-")
        if j1 == 1 and j2 == 2:
            print("*-")
            w1 = 1
            Donald['Tricks']+=1
            Donald['Aces']+=1
        elif j1 ==2 and j2 == 1:
            print("*--")
            w2 = 1
            joe['Tricks']+=1
            joe['Aces']+=1
        else:
            print("*---")
            w1 = 1
            Donald['Tricks']+=1
    if w1 == 1:
        if li == 0:
            c1.append(" ".join(t1))
            c1.append(" ".join(t2))
            
        else:
            for i in range(0,len(li),1):
                c1.append(li[i])
    if w2 == 1:
        if li == 0:
            c2.append(" ".join(t1))
            c2.append(" ".join(t2))
        else:
            for i in range(0,len(li),1):
                c2.append(li[i])
        

Donald={"Tricks":0, "Challenges": 0, "Aces": 0}
joe={"Tricks":0, "Challenges": 0, "Aces": 0}

match(c1, c2) 


# Debug section

# In[249]:


print(Donald, joe)


# In[240]:


match(c1, c2)


# In[226]:


print(len(c1),len(c2))


# In[ ]:





# In[ ]:




