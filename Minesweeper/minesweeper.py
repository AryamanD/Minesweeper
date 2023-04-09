import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
from tkinter import *
from PIL import ImageTk,Image
check=0
f=0
window=Tk()
window.title("Minesweeper")
window.iconbitmap("C:/Users/ginge/Documents/PROGRAMMING/Python/Mini Project/mine1.ico")
window.resizable(0,0)
Mines=[[0]*9 for i in range(9)]
Listi=[]
Listj=[]
min1=min2=sec1=sec2=0
t=0
def SetMines():
    global Mines
    f=open("C:/Users/ginge/Documents/PROGRAMMING/Python/Mini Project/Fieldnumber.txt","r")
    r=f.readline(1)
    f.close()
    f=open("C:/Users/ginge/Documents/PROGRAMMING/Python/Mini Project/Minecord.txt","r")
    j=1
    while j<=int(r):
        Field=f.readline()
        j=j+1
    i=0
    while i<20:
        Mines[int(Field[i])][int(Field[i+1])]=9
        i=i+2
    f.close()
    if int(r)!=5:
        r=int(r)+1
    else:
        r=1
    f=open("C:/Users/ginge/Documents/PROGRAMMING/Python/Mini Project/Fieldnumber.txt","w")
    f.write(str(r))
    f.close()
def Minefield():
    SetMines()
    global Mines
    i=0
    while i<9:
        j=0
        while j<9:
            if Mines[i][j]==9:
                if j+1!=9:
                    if Mines[i][j+1]!=9:Mines[i][j+1]+=1
                if j-1!=-1:
                    if Mines[i][j-1]!=9:Mines[i][j-1]+=1
                if i+1!=9:
                    if Mines[i+1][j]!=9:Mines[i+1][j]+=1
                if i-1!=-1:
                    if Mines[i-1][j]!=9:Mines[i-1][j]+=1
                if j+1!=9 and i-1!=-1:
                    if Mines[i-1][j+1]!=9:Mines[i-1][j+1]+=1
                if j-1!=-1 and i+1!=9:
                    if Mines[i+1][j-1]!=9:Mines[i+1][j-1]+=1
                if i+1!=9 and j+1!=9:
                    if Mines[i+1][j+1]!=9:Mines[i+1][j+1]+=1
                if i-1!=-1 and j-1!=-1:
                    if Mines[i-1][j-1]!=9:Mines[i-1][j-1]+=1
            j+=1
        i+=1
def Resetboard():
    global min1,min2,sec1,sec2,t,c
    global Listi
    global Listj
    min1=min2=sec1=sec2=0
    i=0
    t=1
    c=0
    Listi=[]
    Listj=[]
    Time.config(text=str(min1)+str(min2)+":"+str(sec1)+str(sec2))
    while i<9:
        j=0
        while j<9:
            button=Button(window,padx=20,pady=7,command=lambda m=i,n=j:Click(m,n),state=ACTIVE)
            Buttonlist.append(button)  
            button.grid(row=4+i,column=j) 
            Mines[i][j]=0
            j=j+1
        i=i+1
    Time.config(text=str(min1)+str(min2)+":"+str(sec1)+str(sec2))
    Minefield()
def blankcode(m,n):
    if Mines[m][n]!=9:
        if Mines[m][n]!=0 and Mines[m][n]!=8:
            if Mines[m][n]==1:
                Spot3=Button(window,text=str(Mines[m][n]),bg="white",padx=15,pady=6,state=DISABLED)
                Spot4=Label(window,bg="white",fg="blue",text=str(Mines[m][n]),padx=6,pady=5,font=("Arial",12))
            if Mines[m][n]==2:
                Spot3=Button(window,text=str(Mines[m][n]),bg="white",padx=15,pady=6,state=DISABLED)
                Spot4=Label(window,bg="white",fg="green",text=str(Mines[m][n]),padx=6,pady=5,font=("Arial",12))
            if Mines[m][n]>2:
                Spot3=Button(window,text=str(Mines[m][n]),bg="white",padx=15,pady=6,state=DISABLED)
                Spot4=Label(window,bg="white",fg="red",text=str(Mines[m][n]),padx=6,pady=5,font=("Arial",12))
            Spot3.grid(row=m+4,column=n)
            Spot4.grid(row=m+4,column=n)
            Listi.append(m)
            Listj.append(n)
        elif Mines[m][n]!=8:
            Spot3=Button(window,text=str(Mines[m][n]),bg="white",padx=15,pady=6,state=DISABLED)
            Spot4=Label(window,bg="white",padx=6,pady=5,font=("Arial",12))
            Spot3.grid(row=m+4,column=n)
            Spot4.grid(row=m+4,column=n)  
            Mines[m][n]=8
            Listi.append(m)
            Listj.append(n)
            blank(m,n)
def blank(m,n):
    if n+1!=9:
        blankcode(m,n+1)
    if n-1!=-1:
        blankcode(m,n-1)
    if m+1!=9:
        blankcode(m+1,n)
    if m-1!=-1:
        blankcode(m-1,n)
    if n+1!=9 and m+1!=9:
        blankcode(m+1,n+1)
    if m-1!=-1 and n-1!=-1:
        blankcode(m-1,n-1)       
    if n+1!=9 and m-1!=-1:
        blankcode(m-1,n+1)
    if n-1!=-1 and m+1!=9:
        blankcode(m+1,n-1)
space1=Label(window,height=1)
space2=Label(window,height=1)
Time=Label(window,text="00:00",bg="white",font=("Arial",12))
Goal=Label(window,text="Uncover all the safe spots to win!",font=("Arial",10,"italic"))
GoBack=ImageTk.PhotoImage((Image.open("C:/Users/ginge/Documents/PROGRAMMING/Python/Mini Project/backicon.jpg")).resize((47,47)))
Reset=ImageTk.PhotoImage((Image.open("C:/Users/ginge/Documents/PROGRAMMING/Python/Mini Project/reseticon.jpg")).resize((47,47)))
Mine=ImageTk.PhotoImage((Image.open("C:/Users/ginge/Documents/PROGRAMMING/Python/Mini Project/mine.jpg")).resize((47,47)))
GoBackb=Button(window,image=GoBack)
Resetb=Button(window,image=Reset,command=Resetboard)
space1.grid(row=0,column=0,columnspan=9)
GoBackb.grid(row=1,column=1)
Resetb.grid(row=1,column=4)
Time.grid(row=1,column=7,columnspan=2,sticky="w")
space2.grid(row=2,column=0,columnspan=9)
Goal.grid(row=3,column=0,columnspan=9)   
def clock():
    global t
    global min1,min2,sec1,sec2
    sec2=sec2+1
    if sec2==60:
        sec2=0
        min2=min2+1
        if min2<10:
            Time.config(text=str(min1)+str(min2)+":"+str(sec1)+str(sec2))
        elif min2>=10:
            Time.config(text=str(min2)+":"+str(sec1)+str(sec2))
    elif sec2<10 and min2<10:
        Time.config(text=str(min1)+str(min2)+":"+str(sec1)+str(sec2))
    elif sec2<10 and min2>=10:
        Time.config(text=str(min2)+":"+str(sec1)+str(sec2))
    elif sec2>=10 and min2<10:
        Time.config(text=str(min1)+str(min2)+":"+str(sec2))
    elif sec2>=10 and min2>=10:
        Time.config(text=str(min2)+":"+str(sec2))
    if t==0:
        Time.after(1000,clock)
def Window1():
    global window
    global check
    if check==0:
        window.destroy()
window.protocol('WM_DELETE_WINDOW',lambda:Window1())                            
def Reenable(lose):
    global check
    Resetb=Button(window,image=Reset,command=Resetboard)
    GoBackb=Button(window,image=GoBack)
    GoBackb.grid(row=1,column=1)
    Resetb.grid(row=1,column=4)
    check=0
    lose.destroy()
def Window2():
    lose=Tk()
    lose.title("Minesweeper")
    lose.iconbitmap("C:/Users/ginge/Documents/PROGRAMMING/Python/Mini Project/mine1.ico")
    lose.resizable(0,0)
    lose.protocol('WM_DELETE_WINDOW',lambda:Reenable(lose))
    oops=Label(lose,text="Oops! You clicked on a Mine!",font=("Arial",9))
    gover=Label(lose,text="Game over!",pady=1,font=("Arial",10,"bold"))
    Ok=Button(lose,text="OK",width=5,command=lambda:Reenable(lose))
    oops.grid(row=0,column=0,padx=80,pady=5)
    gover.grid(row=1,column=0,pady=5)
    Ok.grid(row=2,column=0,pady=5)
    lose.mainloop()
def delay():
    for t in range(700):
        print(t)
def showlabel(g,h,Spot1,Spot2):
    Spot1=Button(window,text=str(9),bg="white",padx=15,pady=6,state=DISABLED)
    Spot2=Label(window,image=Mine)
    Spot1.grid(row=g+4,column=h)
    Spot2.grid(row=g+4,column=h)
def Win():
    win=Tk()
    win.title("Minesweeper")
    win.iconbitmap("C:/Users/ginge/Documents/PROGRAMMING/Python/Mini Project/mine1.ico")
    win.resizable(0,0)
    win.protocol('WM_DELETE_WINDOW',lambda:Reenable(win))
    congrats=Label(win,text="Congratulations! You Won!!",pady=10,padx=65,font=("Arial",10,"bold"))
    Ok=Button(win,text="OK",width=5,command=lambda:Reenable(win))
    Ok.grid(row=1,column=0,pady=5)
    congrats.grid(row=0,column=0)
    win.mainloop()
c=0
def Click(m,n):
    global c,t
    global f
    global check
    Spot1=Button(window,text=str(Mines[m][n]),bg="white",padx=15,pady=6,state=DISABLED)
    if Mines[m][n]!=9:
        if c==0:
            t=0
            clock()
        c=c+1
        if Mines[m][n]==0:
            Spot2=Label(window,bg="white",padx=6,pady=5,font=("Arial",12))
            Spot1.grid(row=m+4,column=n)
            Spot2.grid(row=m+4,column=n) 
            Listi.append(m)
            Listj.append(n)
            blank(m,n) 
        if Mines[m][n]==1:
            Spot2=Label(window,text=str(Mines[m][n]),fg="blue",bg="white",padx=6,pady=5,font=("Arial",12))
            Spot1.grid(row=m+4,column=n)
            Spot2.grid(row=m+4,column=n)
            Listi.append(m)
            Listj.append(n)
        if Mines[m][n]==2:
            Spot2=Label(window,text=str(Mines[m][n]),fg="green",bg="white",padx=6,pady=5,font=("Arial",12))
            Spot1.grid(row=m+4,column=n)
            Spot2.grid(row=m+4,column=n)
            Listi.append(m)
            Listj.append(n)
        if Mines[m][n]>2 and Mines[m][n]<8:
            Spot2=Label(window,text=str(Mines[m][n]),fg="red",bg="white",padx=6,pady=5,font=("Arial",12))
            Spot1.grid(row=m+4,column=n)
            Spot2.grid(row=m+4,column=n)
            Listi.append(m)
            Listj.append(n)
    else:
        t=1
        Spot2=Label(window,image=Mine)
        Spot2.grid(row=m+4,column=n)
        i=0
        while i<9:
            j=0
            while j<9:
                if Mines[i][j]==9:
                    window.after(250,lambda g=i,h=j:showlabel(g,h,Spot1,Spot2))
                else:
                    l=0
                    flag=0
                    while l<len(Listi):
                        if i==Listi[l] and j==Listj[l]:
                            flag=flag+1
                        l=l+1
                    if flag==0:
                        Spotd=Button(window,padx=20,pady=6,state=DISABLED)
                        Spotd.grid(row=i+4,column=j)
                j=j+1
            i=i+1
        Resetb=Button(window,image=Reset,state=DISABLED)
        GoBackb=Button(window,image=GoBack,state=DISABLED)
        GoBackb.grid(row=1,column=1)
        Resetb.grid(row=1,column=4)
        check=1
        Window2()
    i=0;count=0
    while i<9:
        j=0
        while j<9:
            l=0
            while l<len(Listi):
                if i==Listi[l] and j==Listj[l]:
                    count=count+1
                    break
                l=l+1
            j=j+1
        i=i+1
    if 81-count==10:
        t=1
        count=0
        Resetb=Button(window,image=Reset,state=DISABLED)
        GoBackb=Button(window,image=GoBack,state=DISABLED)
        GoBackb.grid(row=1,column=1)
        Resetb.grid(row=1,column=4)
        check=1
        i=0
        while i<9:
            j=0
            while j<9:
                if Mines[i][j]==9:
                    Spotd=Button(window,padx=20,pady=6,state=DISABLED)
                    Spotd.grid(row=i+4,column=j)
                j=j+1
            i=i+1      
        Win()
Buttonlist=[]
Resetboard()
window.mainloop()