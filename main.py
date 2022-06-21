# Python for backend stuff...
# Made and Designed by Navaneeth
# This application is strictly for my school project.
# Lesson -> Employability Skills > Unit 3
# These questions are strictly based on the latest NCERT book.

# Thank you for using this, user!

from tkinter import *
from tkinter import messagebox as mb
from tkinter.messagebox import askyesno, askokcancel
import json

root = Tk()
root.geometry("800x500")
root.title("Quiz - School Project")

with open('quiz.json') as f:
    obj = json.load(f)
q = (obj['ques'])
options = (obj['options'])
a = (obj['ans'])

class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="Quiz in ICT Skills", width=50, bg="blue", fg="white", font=("Arial", 20, "bold"))
        t.place(x=0, y=2)
        fsdis = Label(root, text="Fullscreen-disabled", font=("times", 10))
        fsdis.place(x=0, y=470)
        navmsg = Label(root, text="-Made by Navaneeth", font=("times", 10))
        navmsg.place(x=670, y=470)
        qn = Label(root, text=q[qn], width=60, font=("times", 15, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    """
Radio buttons are buttons that we choose as the correct option, in this case: the answer.
They play a very important role in this quiz as they help us select the correct answers, rather than 
us typing the correct answer and getting the spelling wrong.

First, set a value to the radio button, in this case, its 0.
Then set the value for the boxes as an empty list.
The set the y position of the radio buttons as 150.

    while value < 4:
        button = SetRadioButton(root, text=" ", variable = self.option_selected, value = value + 1, font=("times", 14))
        b.append(btn)
        btn.place(x=100, y=yp)
        Add the y position of the radio button upto 40, in this case: yp += 40

    return the value of "b"
    return b

    """

    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("comicsansms", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 50
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10, bg="green", fg="white",
                         font=("times", 16, "bold"))
        nbutton.place(x=300, y=380)
        quitbutton = Button(root, text="Quit", command=self.confirm, width=10, bg="red", fg="white",
                            font=("times", 16, "bold"))
        quitbutton.place(x=500, y=380)
        backbutton = Button(root, text="Back", command=self.backbtn, width=10, bg="yellow", fg="black",
                            font=("times", 16, "bold"))
        backbutton.place(x=100, y=380)

    def confirm(self):
        answer = askyesno(title='Warning!', message='Are you sure that you want to quit? \n'
                                                    '(Tip: Answer all the questions before quitting.)')
        if answer:
            root.quit()

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True

    def backbtn(self):
        if self.qn >= 1:
            self.qn -= 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

quiz = Quiz()
root.mainloop()
