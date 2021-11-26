from tkinter import *
from random import randint
from time import sleep

screen = Tk()
screen.geometry("370x300")
screen.title("Đấm Kéo Lá Game")
screen.maxsize(370, 300)
screen.minsize(370, 300)

randomORG = 0
#funtion
player = ""
computer = ""
ketqua = ""
    
def generateComputerChoice():
        ChoiceNo = randint(0,2)
        if ChoiceNo == 0:
            return "Đấm"
        if ChoiceNo == 1:
            return "Kéo"
        if ChoiceNo == 2:
            return "Lá"
        sleep(1000)

def Rock():
    computer = generateComputerChoice()
    player = "Đấm"
    if computer == player:
        ketqua="Hoà"
        displayLabel.config(text = "Kết quả: Hoà")
        computerButton.config(text = "Đấm")
    if computer == "Lá":
        ketqua = "Thua"
        displayLabel.config(text = "Kết quả: Thua")
        computerButton.config(text = "Lá")
    if computer == "Kéo":
        ketqua = "Thắng"
        displayLabel.config(text = "Kết quả: Thắng")
        computerButton.config(text = "Kéo")

def Paper():
    computer = generateComputerChoice()
    player = "Lá"
    if computer == player:
        ketqua="Hoà"
        displayLabel.config(text = "Kết quả: Hoà")
        computerButton.config(text = "Lá")
    if computer == "Kéo":
        ketqua = "Thua"
        displayLabel.config(text = "Kết quả: Thua")
        computerButton.config(text = "Kéo")
    if computer == "Đấm":
        ketqua = "Thắng"
        displayLabel.config(text = "Kết quả: Thắng")
        computerButton.config(text = "Đấm")

def Scissors():
    computer = generateComputerChoice()
    player = "Kéo"
    if computer == player:
        ketqua="Hoà"
        displayLabel.config(text = "Kết quả: Hoà")
        computerButton.config(text = "Kéo")
    if computer == "Đấm":
        ketqua = "Thua"
        displayLabel.config(text = "Kết quả: Thua")
        computerButton.config(text = "Đấm")
    if computer == "Lá":
        ketqua = "Thắng"
        displayLabel.config(text = "Kết quả: Thắng")
        computerButton.config(text = "Lá")

titleLabel = Label(screen)
titleLabel.grid(columnspan = "3", row = "0", pady="10")
titleLabel.config(text="GAME ĐẤM KÉO LÁ", font=("Segoe ui Bold",18))

computerButton = Label(screen, borderwidth = 2, width="31", height="2")
computerButton.grid(columnspan = "3", row = "1", padx = 20, pady=10)
computerButton.config(text="Vui lòng chọn skills", font=("Playfair display",15), relief=GROOVE, justify="center", width="27")

displayLabel = Label(screen, borderwidth = 2, width="27", height="2")
displayLabel.grid(columnspan = "3", row = "2", padx = 5, pady=10)
displayLabel.config(text="Kết quả", relief=GROOVE, justify="center", font=("Playfair display",15))

RockButton = Button(screen)
RockButton.grid(column = "0", row = "3", padx = (7,0), pady=10)
RockButton.config(text = "Búa", justify="center",width="7", relief=GROOVE, font=("Playfair display",15), command = Rock)

PaperButton = Button(screen)
PaperButton.grid(column = "1", row = "3", pady=10)
PaperButton.config(text = "Lá", justify="center",width="7", relief=GROOVE, font=("Playfair display",15), command = Paper)

ScissorsButton = Button(screen)
ScissorsButton.grid(column = "2", row = "3",padx=(0,7), pady=10)
ScissorsButton.config(text = "Kéo", justify="center",width="7", relief=GROOVE, font=("Playfair display",15), command = Scissors)


screen.mainloop()