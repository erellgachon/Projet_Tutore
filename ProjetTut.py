from tkinter import *
import random
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
        
                   
def permutationAleatoire(n) :
    tab=[]
    for i in range(n) :
        tab.append((i,random.uniform(0,1)))
    tabSorted=sorted(tab, key=lambda x : x[1])
    permutation=[element[0] for element in tabSorted]
    return permutation

def RS() :
    fenetre=Tk()
    fenetre.title("On est trop forts <3")
    size=800
    can=Canvas(fenetre,width=size,height=size, bg="white")
    can.pack()
    print("Mode : 'al' pour permutation aléatoire, 'man' pour la rentrer à la main")
    mode=str(input("Mode = "))
    n=int(input("n = "))
    if (mode=='al') :
        permut=permutationAleatoire(n)
    else :
        permut=[]
        for i in range (n) :
            print("Sur quoi envoie",i+1,end='')
            permut.append(int(input(" ? : ")))


    
    [P,Q]=PermutationToYoung(permut)  #Tab de Young
    squareSize=size//max(len(P),len(P[0]))
    for j in range(len(P)) :
        y=0 #affichage
        for i in range(0,len(P[j])) :
            can.create_rectangle(y,j*squareSize,squareSize+y,squareSize+j*squareSize,fill="black")
            can.create_rectangle(y+1,j*squareSize+1,(squareSize-1)+y,(squareSize-1)+j*squareSize,fill="white")
            #can.create_text(squareSize//2+y,squareSize//2+j*squareSize,text=P[j][i],fill="blue")
            y=y+squareSize
    '''
    for j in range(len(Q)) :
        y=0 #affichage
        for i in range(0,len(Q[j])) :
            can.create_rectangle(y,j*squareSize+size//2,squareSize+y,squareSize+j*squareSize+size//2,fill="black")
            can.create_rectangle(y+1,j*squareSize+1+size//2,squareSize-1+y,squareSize-1+j*squareSize+size//2,fill="white")
            #can.create_text(squareSize//2+y,squareSize//2+j*squareSize+size//2,text=Q[j][i],fill="blue")
            y=y+squareSize
    '''

    #can.create_text(len(P[0])*50+50,100,font=("Arial",30),text="P",fill="green")
    #can.create_text(len(P[0])*50+50,600,font=("Arial",30),text="Q",fill="green")
