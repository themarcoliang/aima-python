import random

def rand_graph(p,n):
    friendship = {}
    for i in range(0,n):
        friendship[i] = list(())
    for first in range(0,n-1):
        for second in range(first,n):
            if(second in friendship[first] or first == second):
                continue
            else:
                rand = random.randrange(100) / 100
                if(rand <= p): #create link
                    friendship[first].append(second)
                    friendship[second].append(first)
    
    return friendship
            
# graph=rand_graph(0.2,5)
# print(graph)