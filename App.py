from tkinter import *
from ProjetTut import *
from math import *

class App :
    def __init__(self) :
        self.window=Tk()
        self.window.title("Mon application")
        self.font=("Arial",20)
        self.mode="al"
        self.permut=[]
        self.n=0
        self.cpt=0
        self.widgets=[]
        self.menu()
        self.window.mainloop()


    def menu(self) :
        self.cleanWindow()
        manualEntry=Button(self.window, font=self.font , width = 50, text = "Crérer ma permutation", command=lambda : self.parameters("man"))
        manualEntry.grid(row=0)
        randomEntry=Button(self.window, font = self.font, width=50,  text= "Permutation Aléatoire", command = lambda : self.parameters("al"))
        randomEntry.grid(row=1)
        partitionEntry=Button(self.window, font = self.font, width=50,  text= "Diagrammes de Young pour un n", command = lambda : self.parameters("par"))
        partitionEntry.grid(row=2)
        self.widgets.append(partitionEntry)
        self.widgets.append(manualEntry)
        self.widgets.append(randomEntry)

    def cleanWidget(self,widget) :
        widget.grid_remove()
        self.widgets.remove(widget)
        
    def cleanWindow(self) :
        for wid in self.widgets :
            wid.grid_remove()
        self.widgets=[]

    def parameters(self, mode) :
        self.permut=[]
        self.cleanWindow()
        self.mode=mode
        self.chooseN()

    def assign(self,display,i) :
        self.permut.append(i)
        permutLabel=Label(self.window,text=str(i))
        permutLabel.grid(row=self.cpt+1,column=1)
        self.widgets.append(permutLabel)
        self.cleanWidget(display[i-1])
        self.cpt+=1
        if self.cpt-1==self.n :
            self.displayPQButtons(self.n+2)

    def displayPQButtons(self,row) :
        chooseP=Button(self.window, text = "Afficher P", command = lambda :self.display(False)) 
        chooseP.grid(row=row,columnspan=2,pady=8)
        self.widgets.append(chooseP)
        
        if (self.mode=="man") :
            choosePQ=Button(self.window, text = "Afficher P et Q", command = lambda : self.display(True))
            choosePQ.grid(row=row+1,columnspan=2)
            self.widgets.append(choosePQ)

        
    def choosePermutation(self) :
        display=[]
        self.cpt=1
        for i in range(self.n) :
            new=Button(self.window, text=str(i+1), command = lambda i=i: self.assign(display,i+1))
            self.widgets.append(new)
            display.append(new)
            new.grid(row=i+2,column=0)
            

    def chooseN(self) :
        def getN(event) :
            self.n=int(answer.get())
            if self.mode=="par" :
                self.displayPartition()
            elif (self.mode=="man") :
                self.permut=[]
                self.choosePermutation()
            elif (self.mode=="al") :
                  self.permut=[]
                  self.permut=permutationAleatoire(self.n)
                  self.displayPQButtons(2)
            
        choice=Label(self.window, text="Paramètres")
        choice.grid(row=0, columnspan=2, pady=8)
        self.widgets.append(choice)
        answerLabel=Label(self.window, text="n = ")
        answerLabel.grid(row=1,column=0, pady=5, padx=5)
        self.widgets.append(answerLabel)
        answer=Entry(self.window)
        answer.grid(row=1,column=1, pady=5, padx=5)
        self.widgets.append(answer)
        answer.bind("<Return>", getN)



    def restart(self) :
        self.cleanWindow()
        self.menu()

    def is_square(self, apositiveint):
        x = apositiveint // 2
        seen = set([x])
        while x * x != apositiveint:
          x = (x + (apositiveint // x)) // 2
          if x in seen: return False
          seen.add(x)
        return True


    def minCarre(self,a):
        b=a
        while(not self.is_square(b)):
            b+=1
        return b

    def displayPartition(self):
        self.cleanWindow()
        tab=partition(self.n)
        size=800
        can=Canvas(self.window,width=size,height=size, bg="white")
        can.grid()
        self.widgets.append(can)
        restartButton=Button(self.window,text="Restart", command = lambda : self.restart())
        restartButton.grid(row=1)
        self.widgets.append(restartButton)
        
        tabSize = size//int(sqrt(self.minCarre(len(tab))))
        squareSize=tabSize//self.n
        print("tabSize : ", tabSize)
        

        i=0
        jsp = 0
        for partitions in tab :
            if(i+tabSize>size):
                i=0
                jsp = jsp + tabSize + 5
            print("i :",i)
            for j in range(len(partitions)) :
                for y in range(0,partitions[j]*squareSize,squareSize) :
                    can.create_rectangle(y+i,j*squareSize+jsp,squareSize+y+i,squareSize+j*squareSize+jsp,fill="black")
                    can.create_rectangle(y+1+i,j*squareSize+1+jsp,(squareSize-1)+y+i,(squareSize-1)+j*squareSize+jsp,fill="white")
            i=i+tabSize


                
            
    
    def display(self,displayQ) :
        self.cleanWindow()
        size=800
        can=Canvas(self.window,width=size,height=size, bg="white")
        can.grid()
        self.widgets.append(can)
        restartButton=Button(self.window,text="Restart", command = lambda : self.restart())
        restartButton.grid(row=1)
        self.widgets.append(restartButton)

            
        [P,Q]=PermutationToYoung(self.permut)
        if (displayQ) :
            squareSize= size//(2*max(len(P),len(P[0])))-5
        else :
            squareSize=size//max(len(P),len(P[0]))
        font=("Arial",squareSize//4)

        for j in range(len(P)) :
            y=0
            for i in range(0,len(P[j])) :
                can.create_rectangle(y,j*squareSize,squareSize+y,squareSize+j*squareSize,fill="black")
                can.create_rectangle(y+1,j*squareSize+1,(squareSize-1)+y,(squareSize-1)+j*squareSize,fill="white")
                if (self.mode=="man") :
                    can.create_text(squareSize//2+y,squareSize//2+j*squareSize,text=P[j][i],fill="blue",font=font)
                y=y+squareSize
        if (displayQ) :
            for j in range(len(Q)) :
                y=0
                for i in range(0,len(Q[j])) :
                    can.create_rectangle(y,j*squareSize+size//2,squareSize+y,squareSize+j*squareSize+size//2,fill="black")
                    can.create_rectangle(y+1,j*squareSize+1+size//2,squareSize-1+y,squareSize-1+j*squareSize+size//2,fill="white")
                    if (self.mode=="man") :
                        can.create_text(squareSize//2+y,squareSize//2+j*squareSize+size//2,text=Q[j][i],fill="blue",font=font)
                    y=y+squareSize



            
App()
