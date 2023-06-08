#!/usr/bin/env python
# coding: utf-8

# In[79]:


#maths game 2.0 
#1. Import libraries 
#2. Create a class to generate the question
#3. Create a class to display the GUI and widgets 

#import libraries 
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random 
import operator

#class to generate the questions 
class Maths_Question:
#initialize variables to generate question 
    def __init__(self):
        
        self.num1 = random.randint(0,10) 
        self.num2 = random.randint(0,10) 
        self.ops = ["+", "-", "*"]
        self.op = random.choice(self.ops)
        self.sol = int()
        
        if self.op == "-":
           # print("takeaway!", self.num1, self.num2)
            if self.num1 < self.num2:
                self.num1, self.num2 = self.num2, self.num1 
        
    #create question 
    def create_question(self):
        #question
        
        self.question = "What is {} {} {}?".format(self.num1, self.op, self.num2, "\n")   
            
        return self.question
    
    #check answer 
    def solution(self):
        
        if self.op == "+":
            self.sol = self.num1 + self.num2
        elif self.op == "-":
            self.sol = self.num1 - self.num2 
        elif self.op == "*":
            self.sol = self.num1 * self.num2
        
        return self.sol
                      
maths_game=Maths_Question()
maths_game.create_question()


# In[ ]:





# In[80]:


maths_game.solution()


# In[81]:


## class to create the gui !!!

#import libraries 
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

class GUI_Creator: 
    
    def __init__(self):
        
        # Create a GUI Window
        self.gui = Tk()
        
        # set the size of the GUI Window
        self.gui.geometry("800x450")

        # set the title of the Window
        self.gui.title("Let's practise our maths!")
        
        self.title = Label(self.gui, text = "Welcome to the maths game!", 
                      width = 50, bg="blue", fg="white", 
                      font=("ariel", 20, "bold"))
        #pos of title
        self.title.place(x=0, y=0) 
        
        #initialize variables 
        self.q_num = 0 
        self.score = 0 
        #self.turns = 0
        self.my_string_var = StringVar()
        self.finish_button_text = StringVar()
        self.inp = " "
        self.q = " "
        self.a = " "  
        self.maths_game = Maths_Question() 
        
        #gui widgets 
        self.q_number = Label(self.gui, textvariable = self.my_string_var,
                        width = 60,
                        font=("ariel", 16, "bold"), anchor = "w")
        self.q_number.place(x=70, y=100)     
        
        self.user_entry_box = Entry(self.gui, width=15, 
                          font=("ariel", 16, "bold"))
        self.user_entry_box.place(x=70, y=150)
        
        self.enter_button = Button(self.gui, text="Enter", command = self.check_answer,
                                  width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        
        self.msg = Label(self.gui, text = " ", width = 60, font=("ariel", 16, "bold"), anchor = "w")
        self.msg.place(x=60, y =260)
        
        #placing buttons on the screen
        self.enter_button.place(x=350, y=210) 
        
                
        #bind the return key to the window
        self.gui.bind('<Return>', lambda event:self.check_answer())
        
        #call question class function to create question 
        self.assign_question()
    
        #start the GUI
        self.gui.mainloop()

    #method to assign question to my_string_var
    def assign_question(self):
        self.q_num += 1
       #maths_game=Maths_Question()
        self.maths_game = Maths_Question()
        self.q = self.maths_game.create_question()
        self.a = self.maths_game.solution()
        self.my_string_var.set(self.q)  
        print(self.q, self.a)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            
    #method to check the answer 
    def check_answer(self):
        try: 
            inp = int(self.user_entry_box.get())
            if inp == self.a:
                self.score += 1
                self.msg.config(text = "Correct! Score: " + str(self.score))
            else:
                self.msg.config(text = "Incorrect. The answer is " + str(self.a) + ".")

            if self.q_num <10: 
                self.assign_question()
            elif self.q_num == 10: 
                self.enter_button.place_forget()
                self.user_entry_box.place_forget()
                self.my_string_var.set("Round completed!")
                self.finish_button = Button(self.gui, text="Finish", command = self.finish_game, 
                         width=8,bg="blue",fg="white",font=("ariel",12,"bold")) 
                self.finish_button.place(x=350,y=380)
            
                         
        except: 
            self.msg.config(text="Please enter an integer.")
        
        self.user_entry_box.delete(0, END)  
    
    def finish_game(self):
        self.msg.config(text= "Well done! You have completed the quiz! You scored, "+ str(self.score) + " out of "+ str(self.q_num) + ".\n"
                       "Would you like to play again?")
        self.finish_button.place_forget()
        self.q_number.place_forget()
        self.no_button = Button(self.gui, text="No", command = self.exit_game, 
                             width=8,bg="blue",fg="white",font=("ariel",12,"bold")) 
        self.yes_button = Button(self.gui, text="Yes", command = self.restart_game, 
                             width=8,bg="blue",fg="white",font=("ariel",12,"bold")) 
        self.yes_button.place(x=200,y=380)
        self.no_button.place(x=100,y=380)
        
    def restart_game(self):
        self.yes_button.place_forget()
        self.no_button.place_forget()
        #self.next_button.place_forget()
        self.score = 0 
        self.q_num = 0 
        self.assign_question()
        self.q_number.place(x=70, y=100)
        self.user_entry_box.place(x=70, y=150)
        self.enter_button.place(x=350, y=210)
        self.msg.config(text = " ")
        
    def exit_game(self):
        self.gui.destroy()
        self.gui.quit()
        
window=GUI_Creator()
#maths_game=Maths_Question()


# In[ ]:




