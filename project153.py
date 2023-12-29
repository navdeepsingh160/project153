from tkinter import *
import random


root=Tk()
root.title("Password Generator")
root.geometry("400x400")
input_password = Entry(root)
gussed_label =Label(root)
genrated_password = Label(root)


array_3d = [[['1','2','3','4','5','6',"A","B","C",'D','E','F','G','H'],["HEAD","Tail","KING","QUEEN"],["i","j","k","l","m","#","!","@","%"]]]
print(array_3d[0][2][3])

def new_password():
    random_no_1 = random.randint(0,13)
    random_no_2 = random.randint(0,3)
    random_no_3 = random.randint(0,8)
    
    
    letter1 =str(array_3d[0][0][random_no_1])
    letter2 =str(array_3d[0][1][random_no_2])
    letter3 =str(array_3d[0][2][random_no_3])
    gussed_label["text"] = "gussed password - "+ input_password.get()
    genrated_password["text"] = "genrated password - " + letter1 + "" + letter2 + ""  + letter3
    
btn = Button(root, text= "New Password", command = new_password)
btn.place(relx= 0.5, rely=0.5, anchor = CENTER)    

genrated_password.place(relx= 0.5, rely=0.6, anchor = CENTER) 

input_password.place(relx= 0.5, rely=0.3, anchor = CENTER)    
gussed_label.place(relx= 0.5, rely=0.4, anchor = CENTER)    


root.mainloop()