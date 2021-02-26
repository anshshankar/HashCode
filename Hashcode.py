from itertools import combinations
def pizzdist():
    pass



def maxindg(i,lispiz):
    score=0
    pizz=[]
    content=[]
    # (1,0,0) COmbinations  & List of Piiza
    #list pizza
    #list combition
    # permutations
    total=i[0]+i[1]+i[2]
    for i in range()
    


    



    return score,pizz
    






np,t2,t3,t4=input().split()     #First Line Input from User
lispiz=[]                       # Empty List 
np,t2,t3,t4=int(np),int(t2),int(t3),int(t4)
for i in range(0,np):
    a=list(map(str,input().split(" ")))  #List Input from User
    lispiz.append(a)

maxbest=0
bescom=[]
a=[(x,y,z) for x in range(0,t2+1) for y in range(0,t3+1) for z in range(0,t4+1)]
for i in a:
    totalperson=i[0]*2+i[1]*3+i[2]*4
    if(totalperson<=np):
        # Max indigrient to be given to a team
        print(i)
        resco=maxindg(i,lispiz)
        # if(maxbest<resco):
        #     maxbest=resco
        #     bescom=i

        

    else:
        continue




