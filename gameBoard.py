from tkinter import *
from tkinter import messagebox

BUTTON_HEIGHT=3
BUTTON_WIDTH=6

def on_button_click(self,button):
	if button['text'] == ' ':
		if self.player == True:
			button.config(text='X',background='red')
		else:
			button.config(text='O',background='blue')

		self.player = not self.player
		self.turn += 1
		self.update_label()
		self.check_victory()
		

class gameBoard:
	def __init__(self,root):
		self.root = root
		self.player = True
		self.cross_wins = 0
		self.circle_wins = 0
		self.draws = 0
		self.round = 1
		self.turn = 0

		self.button1 = Button(root, text=' ',font = ('Arial',20),height=BUTTON_HEIGHT,width=BUTTON_WIDTH, command=lambda: on_button_click(self,self.button1))
		self.button2 = Button(root, text=' ',font = ('Arial',20),height=BUTTON_HEIGHT,width=BUTTON_WIDTH, command=lambda: on_button_click(self,self.button2))
		self.button3 = Button(root, text=' ',font = ('Arial',20),height=BUTTON_HEIGHT,width=BUTTON_WIDTH, command=lambda: on_button_click(self,self.button3))
		self.button4 = Button(root, text=' ',font = ('Arial',20),height=BUTTON_HEIGHT,width=BUTTON_WIDTH, command=lambda: on_button_click(self,self.button4))
		self.button5 = Button(root, text=' ',font = ('Arial',20),height=BUTTON_HEIGHT,width=BUTTON_WIDTH, command=lambda: on_button_click(self,self.button5))
		self.button6 = Button(root, text=' ',font = ('Arial',20),height=BUTTON_HEIGHT,width=BUTTON_WIDTH, command=lambda: on_button_click(self,self.button6))
		self.button7 = Button(root, text=' ',font = ('Arial',20),height=BUTTON_HEIGHT,width=BUTTON_WIDTH, command=lambda: on_button_click(self,self.button7))
		self.button8 = Button(root, text=' ',font = ('Arial',20),height=BUTTON_HEIGHT,width=BUTTON_WIDTH, command=lambda: on_button_click(self,self.button8))
		self.button9 = Button(root, text=' ',font = ('Arial',20),height=BUTTON_HEIGHT,width=BUTTON_WIDTH, command=lambda: on_button_click(self,self.button9))

		self.label1 = Label(root, font=('Arial',18),text='Round: 0\nX wins: 0\nO wins: 0\ndraws: 0')



	def draw_board(self):
		self.button1.grid(row=0,column=0)
		self.button2.grid(row=0,column=1)
		self.button3.grid(row=0,column=2)

		self.button4.grid(row=1,column=0)
		self.button5.grid(row=1,column=1)
		self.button6.grid(row=1,column=2)

		self.button7.grid(row=2,column=0)
		self.button8.grid(row=2,column=1)
		self.button9.grid(row=2,column=2)

		self.label1.grid(row=0,column=3)

	def update_label(self):
		string = 'Round: ' + str(self.round) + '\nX wins: ' + str(self.cross_wins) + '\nO wins: ' + str(self.circle_wins) + '\ndraws: ' + str(self.draws)
		self.label1.config(text=string)

	def clear(self):
		self.button1.config(text=' ',background='white')
		self.button2.config(text=' ',background='white')
		self.button3.config(text=' ',background='white')
		self.button4.config(text=' ',background='white')
		self.button5.config(text=' ',background='white')
		self.button6.config(text=' ',background='white')
		self.button7.config(text=' ',background='white')
		self.button8.config(text=' ',background='white')
		self.button9.config(text=' ',background='white')

	def check_victory(self):
		#Cross X
		if self.button1['text'] == 'X' and self.button2['text'] == 'X' and self.button3['text'] == 'X' or\
			self.button4['text'] == 'X' and self.button5['text'] == 'X' and self.button6['text'] == 'X' or\
		   	self.button7['text'] == 'X' and self.button8['text'] == 'X' and self.button9['text'] == 'X' or\
\
		  	self.button1['text'] == 'X' and self.button4['text'] == 'X' and self.button7['text'] == 'X' or\
		  	self.button2['text'] == 'X' and self.button5['text'] == 'X' and self.button8['text'] == 'X' or\
		 	self.button3['text'] == 'X' and self.button6['text'] == 'X' and self.button9['text'] == 'X' or\
\
			self.button1['text'] == 'X' and self.button5['text'] == 'X' and self.button9['text'] == 'X' or\
			self.button3['text'] == 'X' and self.button5['text'] == 'X' and self.button7['text'] == 'X':

				messagebox.showinfo("Victory!", "Cross has won!")
				self.cross_wins += 1
				self.update_label()
				self.round += 1
				self.turn = 0
				self.player = not self.round % 2 == 0
				self.clear()

		elif self.button1['text'] == 'O' and self.button2['text'] == 'O' and self.button3['text'] == 'O' or\
			self.button4['text'] == 'O' and self.button5['text'] == 'O' and self.button6['text'] == 'O' or\
		   	self.button7['text'] == 'O' and self.button8['text'] == 'O' and self.button9['text'] == 'O' or\
\
		  	self.button1['text'] == 'O' and self.button4['text'] == 'O' and self.button7['text'] == 'O' or\
		  	self.button2['text'] == 'O' and self.button5['text'] == 'O' and self.button8['text'] == 'O' or\
		 	self.button3['text'] == 'O' and self.button6['text'] == 'O' and self.button9['text'] == 'O' or\
\
			self.button1['text'] == 'O' and self.button5['text'] == 'O' and self.button9['text'] == 'O' or\
			self.button3['text'] == 'O' and self.button5['text'] == 'O' and self.button7['text'] == 'O':

				messagebox.showinfo("Victory!", "Cricle has won!")
				self.circle_wins += 1
				self.update_label()
				self.round += 1
				self.turn = 0
				self.player = not self.round % 2 == 0
				self.clear()

		elif self.turn == 9:

				messagebox.showinfo("Draw!", "Friendship has won!")
				self.draws += 1
				self.update_label()
				self.round += 1
				self.turn = 0
				self.player = not self.round % 2 == 0
				self.clear()
			

		#todo