from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import shutil,os
from dbaccess import Dbhelper
import random

class Quiz:
    # TO INIATE THE GUI

    def __init__(self):
        self._db = Dbhelper()
        self._root = Tk()
        self._root.title("QUIZ TESTER")
        self._root.geometry("600x800")
        self._root.config(background= "#00C1FF")
        self._root.resizable(0,0)

        self._welcome= Label(self._root,text="WELCOME TO QUIZ TESTER",fg="#FF0000",bg="#00C1FF")
        self._welcome.config(font=("Algerian",30,'bold'))
        self._welcome.pack(pady=(20,20))

        imageurl = "images\qlogo.png"
        load = Image.open(imageurl)
        load = load.resize((150, 150), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(image=render, )
        img.image = render
        img.pack(pady=(10,20))

        self._name = Label(self._root,text= "ENTER YOUR NAME",fg= "#000",bg="#00C1FF")
        self._name.config(font=("Times",16))
        self._name.pack(pady=(10,15))

        self._nameInput = Entry(self._root)
        self._nameInput.pack(pady=(10,15),ipadx = 70,ipady= 10)

        self._email = Label(self._root,text="ENTER YOUR EMAIL",fg= "#000",bg="#00C1FF")
        self._email.config(font=("Times",16))
        self._email.pack(pady=(10,15))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(10,15),ipadx=70,ipady=10)

        self._enter = Button(self._root,text="ENTER",fg = "#FFF300",bg = "#FF0000",width= 15,height= 2,command= lambda : self.enter_user())
        self._enter.config(font=("Arial",18))
        self._enter.pack(pady=(10,15))

        self._root.mainloop()


    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()

# TO REGISTER A NEW USER INTO DATABASE. THE OLD USER DATA WILL NOT BE REGISTERED AGAIN BUT CAN PLAY
    def enter_user(self):
        self._name = self._nameInput.get()
        self._email = self._emailInput.get()
        self.generate()
        self._user_answers = []

        if len(self._name)>0 and len(self._email)>0:
            flag = self._db.enter_user(self._name,self._email)

            if flag == 1:
                self.clear()
                self.same_user()
            else:
                messagebox.showerror("ERROR","SORRY SOMETHING WENT WRONG. PLEASE TRY AGAIN")
        else:
            messagebox.showerror("ERROR","PLEASE GIVE YOUR CORRECT CREDENTIALS")

# TO LOAD THE INTRODUCTION AND INSTRUCTION PAGE
    def load_quiz_window(self):
        self._readylabel = Label(self._root,text = "READY TO START ?",fg= "#FF0000",bg="#00C1FF")
        self._readylabel.config(font=("Algerian",30,'bold'))
        self._readylabel.pack(pady=(30,20))

        self._introlabel = Label(self._root,fg ="#FF5100",bg="#00C1FF")
        self._introlabel.config(text = "HI " + str(self._name) + " ARE YOU READY FOR THE QUIZ TEST ?",wraplength = 400)
        self._introlabel.config(font=("Algerian",18,'bold'),justify = "center")
        self._introlabel.pack(pady=(10,10))

        self._readylabel = Label(self._root, text="YOUR LAST TIME SCORE WAS " + str(self.prev_score) + " WANT TO DO BETTER THIS TIME ? GOOD LUCK !",fg="#B900FF",bg="#00C1FF",wraplength = 500)
        self._readylabel.config(font=("Times",16,'bold'))
        self._readylabel.pack(pady=(0, 0))

        self._followlabel = Label(self._root, text="CAREFULLY FOLLOW THE\n INSTRUCTIONS BEFORE STARTING !",fg="#FF0000", bg="#00C1FF", justify="center")
        self._followlabel.config(font=("Arial", 16, 'bold'))
        self._followlabel.pack(pady=(10, 20))

        self._inst1label = Label(self._root, text="1. THERE ARE TOTAL 20 QUESTIONS \nTHAT YOU HAVE TO ATTEND",fg="#000", bg="#00C1FF", justify="left")
        self._inst1label.config(font=("Arial", 15))
        self._inst1label.pack(pady=(20, 10), )

        self._inst2label = Label(self._root, text="      2. ALL QUESTIONS CONSISTS OF 5 (FIVE)\n         MARKS EACH",fg="#000", bg="#00C1FF", justify="left")
        self._inst2label.config(font=("Arial", 15))
        self._inst2label.pack(pady=(8, 10))

        self._inst3label = Label(self._root, text="3. ALL QUESTIONS ARE COMPULSORY", fg="#000", bg="#00C1FF",justify="left")
        self._inst3label.config(font=("Arial", 15))
        self._inst3label.pack(pady=(8, 10))

        self._inst4label = Label(self._root, text="4. ALL ARE MCQ TYPE QUESTIONS", fg="#000", bg="#00C1FF",justify="left")
        self._inst4label.config(font=("Arial", 15))
        self._inst4label.pack(pady=(8, 10))

        self._inst5label = Label(self._root, text="5. CLICK THE START BUTTON WHEN \n    YOU ARE READY", fg="#000",bg="#00C1FF", justify="left")
        self._inst5label.config(font=("Arial", 15))
        self._inst5label.pack(pady=(8, 10))

        self._start = Button(self._root, text="START QUIZ", fg="#FFF300", bg="#FF0000", width=15, height=2,command=lambda: self.start_quiz())
        self._start.config(font=("Arial", 10))
        self._start.pack(pady=(10, 15))
# TO SHOW THE PREVIOUS SCORED MARKS OF AN OLD USER AND INSTRUCTION PAGE
    def same_user(self):
        self.x = self._db.same_user(self._name,self._email)
        if self.x[0][0]>0:
            self.prev_score = self.x[0][0]
            self.load_quiz_window()
        else:
            self._readylabel = Label(self._root, text="READY TO START ?", fg="#FF0000", bg="#00C1FF")
            self._readylabel.config(font=("Algerian", 30, 'bold'))
            self._readylabel.pack(pady=(30, 20))

            self._introlabel = Label(self._root, fg="#FF5100", bg="#00C1FF")
            self._introlabel.config(text="HI " + str(self._name) + " ARE YOU READY FOR THE QUIZ TEST ?", wraplength=400)
            self._introlabel.config(font=("Algerian", 18, 'bold'), justify="center")
            self._introlabel.pack(pady=(10, 10))

            self._followlabel = Label(self._root, text="CAREFULLY FOLLOW THE\n INSTRUCTIONS BEFORE STARTING !",fg="#FF0000", bg="#00C1FF", justify="center")
            self._followlabel.config(font=("Arial", 16, 'bold'))
            self._followlabel.pack(pady=(10, 20))

            self._inst1label = Label(self._root, text="1. THERE ARE TOTAL 20 QUESTIONS \nTHAT YOU HAVE TO ATTEND",fg="#000", bg="#00C1FF", justify="left")
            self._inst1label.config(font=("Arial", 15))
            self._inst1label.pack(pady=(20, 10), )

            self._inst2label = Label(self._root, text="      2. ALL QUESTIONS CONSISTS OF 5 (FIVE)\n         MARKS EACH",fg="#000", bg="#00C1FF", justify="left")
            self._inst2label.config(font=("Arial", 15))
            self._inst2label.pack(pady=(8, 10))

            self._inst3label = Label(self._root, text="3. ALL QUESTIONS ARE COMPULSORY", fg="#000", bg="#00C1FF",justify="left")
            self._inst3label.config(font=("Arial", 15))
            self._inst3label.pack(pady=(8, 10))

            self._inst4label = Label(self._root, text="4. ALL ARE MCQ TYPE QUESTIONS", fg="#000", bg="#00C1FF",justify="left")
            self._inst4label.config(font=("Arial", 15))
            self._inst4label.pack(pady=(8, 10))

            self._inst5label = Label(self._root, text="5. CLICK THE START BUTTON WHEN \n    YOU ARE READY", fg="#000",bg="#00C1FF", justify="left")
            self._inst5label.config(font=("Arial", 15))
            self._inst5label.pack(pady=(8, 10))

            self._start = Button(self._root, text="START QUIZ", fg="#FFF300", bg="#FF0000", width=15, height=2,command=lambda: self.start_quiz())
            self._start.config(font=("Arial", 10))
            self._start.pack(pady=(10, 15))
# TO LOAD QUESTIONS AND ANSWERS
    def start_quiz(self,i = 0):
        self.clear()

        self._questions = [
            "Q.1. WHO IS THE FIRST PRESIDENT OF INDIA ?",
            "Q.2. WHO IS THE FIRST PRESIDENT OF USA ?",
            "Q.3. The 'Dalong Village' covering an area of 11.35 sq. km. has recently (May 2017) been declared as Biodiversity Heritage Site under Section 37(1) of Biological Diversity Act, 2002. The village is situated in the Indian State of -",
            "Q.4.  ........... is the first woman to head a public sector bank.",
            "Q.5. World Tourism Day is celebrated on-",
            "Q.6. QWhere is Bose Institute?",
            "Q.7. When is the International Yoga Day celebrated?",
            "Q.8. When Government of India confers the Highest Civilian Honor for Women by presenting Nari Shakti Puraskars ?",
            "Q.9. The motif of 'Hampi with Chariot' is printed on the reverse of which currency note?",
            "Q.10 Election Commission of India has decided that the voter's identification shall be mandatory in the elections at the time of poll. Which of the following shall be the main document of identification of a voter?",
            "Q.11 'Line of Blood' is a book written by whom?",
            "Q.12 Which player scored the fastest hat-trick in the Premier League?",
            "Q.13 Which player, with 653 games, has made the most Premier League appearances?",
            "Q.14 Three players share the record for most Premier League red cards (8). Who are they?",
            "Q.15 With 260 goals, who is the Premier League's all-time top scorer?",
            "Q.16 When was the inaugural Premier League season?",
            "Q.17 Which team won the first Premier League title?",
            "Q.18 What's the biggest animal in the world?",
            "Q.19 Which country is brie cheese originally from?",
            "Q.20 What is the capital of Iceland?"
        ]

        self._answers = [
            ["RAJENDRA PRASAD", "A.P.J ABDUL KALAM", "RAMNATH KOVIND", "PRANAB MUKHERJEE"],
            ["GEORGE WASHINGTON", "HITLER", "GEORGE BUSH", "ABRAHAM LINCOLN"],
            ["Manipur", "Madhya Pradesh", "Mizoram", "Maharashtra"],
            ["Arundhati Bhattacharya", "Shikha Sharma", "Chanda Kochar", "Usha Ananthasubramanyan"],
            ["September 12", "September 25", "September 27", "September 29"],
            [" Dispur", "Kolkata", "Mumbai", "New Delhi"],
            ["June 21", "March 21", "April 22", "May 31"],
            ["June 5", "8th March, every year, International Women's Day", "June 21", "April 7"],
            ["One Rupee Note", "Rs. 500 note", "Rs. 50 note", "Rs. 1000 note"],
            ["Voter Slip", "Electoral Photo Identity Cards (EPIC)", "Indelible ink mark", "Electoral rolls"],
            ["Bairaj Khanna", "Ursula Vernon", "Amal EI-Mohtar", "Diksha Basu"],
            ["SADIO MANE", "C.RONALDO", "D.BECKHAM", "LIONEL MESSI"],
            ["Gareth Barry", "FABIO", "GARETH BALE", "ASENSIO"],
            ["Patrick Vieira,Richard Dunne and Duncan Ferguson", "MESSI,RONALDO AND NEYMAR",
             "RAMOS, CARVAJAL AND VIDAL", "FABIO,ISCO AND BALE"],
            ["Alan Shearer", "EDEN HAZARD", "D.BECKHAM", "WAYNE ROONEY"],
            ["1992-93", "1993-94", "1990-91", "1998-99"],
            ["MANCHESTER UNITED", "MANCHESTER CITY", "CHELSEA", "TOTENHAM"],
            ["BLUE WHALE", "ELEPHANT", "WHITE SHARK", "KILLER WHALE"],
            ["FRANCE", "ITALY", "BRAZIL", "SPAIN"],
            ["Reykjavík", "ZURICH", "PARIS", "QATAR"]
        ]

        self._correct_answers = [0,0,1,0,2,1,0,1,2,1,0,0,0,0,0,0,0,0,0,0]


        self._question_label = Label(self._root,text = self._questions[self._index[i]],width = 500,justify = "left",wraplength = 500,fg = "#FF0000",bg = "#00C1FF")
        self._question_label.config(font=("Arial",20,'bold'))
        self._question_label.pack(pady=(50,20),padx = (40,40))

        self._radio = IntVar()
        self._radio.set(-1)

        r1 = Radiobutton(self._root,text = self._answers[self._index[i]][0],variable = self._radio,value = 0,fg="#FF00B9",bg="#00C1FF",wraplength = 400,justify = "center",command = lambda :self.next_questions(i+1))
        r1.config(font=("Algerian",18,'bold'))
        r1.pack(pady = (20,50),padx = (50,50))

        r2 = Radiobutton(self._root, text= self._answers[self._index[i]][1], variable=self._radio,value = 1,fg="#FF00B9",bg="#00C1FF",wraplength = 400,justify = "center",command = lambda :self.next_questions(i+1))
        r2.config(font=("Algerian", 18,'bold'))
        r2.pack(pady=(0, 50), padx=(50,50))

        r3 = Radiobutton(self._root, text= self._answers[self._index[i]][2], variable=self._radio,value = 2,fg="#FF00B9",bg="#00C1FF",wraplength = 400,justify = "center",command = lambda :self.next_questions(i+1))
        r3.config(font=("Algerian", 18,'bold'))
        r3.pack(pady=(0, 50), padx=(50,50))

        r4 = Radiobutton(self._root, text= self._answers[self._index[i]][3], variable=self._radio,value = 3,fg="#FF00B9",bg="#00C1FF",wraplength = 400,justify = "center",command = lambda :self.next_questions(i+1))
        r4.config(font=("Algerian", 18,'bold'))
        r4.pack(pady=(0, 50), padx=(50,50))
# TO GENERATE RANDOM QUESTION ORDER FOR DIFFERENT USERS
    def generate(self):
        self._index = []

        while(len(self._index) < 20):
            x = random.randint(0,19)
            if x in self._index:
                continue
            else:
                self._index.append(x)
                

 # TO COLLECT THE ANSWERS FROM USERS
    def next_questions(self,i = 0):
        self._x = self._radio.get()
        self._user_answers.append(self._x)

        if i == 0:
            self.clear()
            self.start_quiz(i= 0)

        else:
            if i == len(self._index):
                self.calculate_result()


            else:
                self.clear()
                self.start_quiz(i = i)

# TO CALCULATE THE RESULT
    def calculate_result(self):
        self.clear()
        self._ans_index = 0
        self._score = 0

        for i in self._index:
            if self._user_answers[self._ans_index] == self._correct_answers[i]:
                self._score = self._score + 5

            self._ans_index = self._ans_index + 1

        self.enter_score()

# TO SHOW THE RESULT OF THE USER
    def show_my_result(self):

        self._score_label1 = Label(self._root, text="END OF QUIZ", fg="#FF00B9",bg="#00C1FF")
        self._score_label1.config(font=("Algerian", 20,'bold'), justify="center")
        self._score_label1.pack(pady=(50, 10))


        self._score_label = Label(self._root,text = str(self._name) + " YOU HAVE SCORED " + str(self._score) + "  OUT OF 100 MARKS",fg= "#FF0000",bg="#00C1FF",wraplength = 500)
        self._score_label.config(font = ("Algerian",20,'bold'),justify = "center")
        self._score_label.pack(pady = (20,10))

        if self._score >= 80:
            imageurl = "images\success.png"
            load = Image.open(imageurl)
            load = load.resize((300, 300), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(image=render,border = 0)
            img.image = render
            img.pack(pady=(20, 20))

            self._score_label1 = Label(self._root, text= "YOU ARE A GREAT PARTICIPANT. EXCELLENT !", fg="#FF00B9", bg="#00C1FF")
            self._score_label1.config(font=("Algerian", 18,'bold'), justify="center")
            self._score_label1.pack(pady=(10,10))

            self._enter = Button(self._root, text="EXIT", fg="#FFF300", bg="#FF0000", width=15, height=2,command=lambda: self.exit_quiz())
            self._enter.config(font=("Arial", 10))
            self._enter.pack(pady=(10, 15))

        elif self._score < 80 and self._score >= 50:
            imageurl = "images\medium.jpg"
            load = Image.open(imageurl)
            load = load.resize((300, 300), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(image=render,border = 0 )
            img.image = render
            img.pack(pady=(20,20))

            self._score_label1 = Label(self._root, text="YOU ARE A MEDIOCRE PARTICIPANT. NEED MORE PRACTICE TO CRACK !", fg="#FF00B9",bg="#00C1FF",wraplength = 500)
            self._score_label1.config(font=("Algerian", 18,'bold'), justify="center")
            self._score_label1.pack(pady=(10,10))

            self._enter = Button(self._root, text="EXIT", fg="#FFF300", bg="#FF0000", width=15, height=2,command=lambda: self.exit_quiz())
            self._enter.config(font=("Arial", 10))
            self._enter.pack(pady=(10, 15))

        else:
            imageurl = "images\work.jpeg"
            load = Image.open(imageurl)
            load = load.resize((300, 300), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(image=render,border = 0)
            img.image = render
            img.pack(pady=(20,20))

            self._score_label1 = Label(self._root, text="YOU ARE ACTUALLY NOT READY FOR THIS QUIZ TEST. NEED TO WORK HARD !",fg="#FF00B9", bg="#00C1FF", wraplength=500)
            self._score_label1.config(font=("Algerian", 18,'bold'), justify="center")
            self._score_label1.pack(pady=(10,10))

            self._enter = Button(self._root, text="EXIT", fg="#FFF300", bg="#FF0000", width=15, height=2,command=lambda: self.exit_quiz())
            self._enter.config(font=("Arial",10))
            self._enter.pack(pady=(10, 15))

# TO UPDATE THE RESULT SCORED BY USER IN THE DATABASE AGAINST THE USER
    def enter_score(self):

        flag = self._db.enter_score(self._score,self._email)
        if flag == 1:
            self.show_my_result()
        else:
            messagebox.showerror("ERROR","SORRY SOME PROBLEM OCCURED. PLEASE GIVE ANOTHER TRY")

# TO EXIT THE QUIZ
    def exit_quiz(self):
        self._root.destroy()










































obj = Quiz()