from tkinter import *
#Sens direct de la bijection entre une permutation et deux tableaux de Young

def PermutationToYoung(tab) :
    P=[[]]
    Q=[[]]
    for i in range(len(tab)) :
        x,y=insert(tab[i],P)
        if (x==len(Q)) :
            Q.append([])
        Q[x].append(i+1)
    return [P,Q]

def FindX(tab,X) :
    for i in range(len(tab)) :
        for j in range(len(tab[i])) :
            if tab[i][j]==X :
                return i,j
    return -1,-1

def YoungToPermutation(P,Q,n) :
    permutation=[]
    for x in range(n,0,-1) :
        i,j=FindX(Q,x)
        print(i,j)
        elt=insertInv(P,i,j)
        if (len(P[i])==0) :
            P.remove([])
        permutation.insert(0,elt)
        print("Permutation",permutation)
        print("P",P)
        print("Q",Q)
    return permutation

def insertInv(P,i,j) :
    elt=P[i][j]
    P[i].remove(elt)
    i1=i-1
    while (i1>=0):
        j1=len(P[i1])-1
        while (j1>=0 and P[i1][j1]>=elt) :
            j1=j1-1
        tmp=P[i1][j1]
        P[i1][j1]=elt
        elt=tmp
        i1=i1-1
    return elt
    
def insert(elmt,tab,i=0) :
    j=0
    if (i==len(tab)) :
        tab.append([])
    while (j<len(tab[i]) and tab[i][j]<elmt) :
        j=j+1
    if (j==len(tab[i])) :
        tab[i].append(elmt)
        return i,j
    else :
        tmp=tab[i][j]
        tab[i][j]=elmt
        return insert(tmp,tab,i+1)
        
                   

    
def RS() :
    fenetre=Tk()
    fenetre.title("On est trop forts <3")
    n=15
    c=50
    can=Canvas(fenetre,width=n*c,height=n*c, bg="white")
    can.pack()

    n=int(input("n = "))
    permut=[]
    for i in range (n) :
        print("Sur quoi envoie",i+1,end='')
        permut.append(int(input(" ? : ")))



    [P,Q]=PermutationToYoung(permut)  #Tab de Young
    for j in range(len(P)) :
        y=0 #affichage
        for i in range(0,len(P[j])) :
            can.create_rectangle(y,j*50,50+y,50+j*50,fill="black")
            can.create_rectangle(y+1,j*50+1,49+y,49+j*50,fill="white")
            can.create_text(25+y,25+j*50,text=P[j][i],fill="blue")
            y=y+50

    for j in range(len(Q)) :
        y=0 #affichage
        for i in range(0,len(Q[j])) :
            can.create_rectangle(y,j*50+500,50+y,50+j*50+500,fill="black")
            can.create_rectangle(y+1,j*50+1+500,49+y,49+j*50+500,fill="white")
            can.create_text(25+y,25+j*50+500,text=Q[j][i],fill="blue")
            y=y+50


    can.create_text(len(P[0])*50+50,100,font=("Arial",30),text="P",fill="green")
    can.create_text(len(P[0])*50+50,600,font=("Arial",30),text="Q",fill="green")
