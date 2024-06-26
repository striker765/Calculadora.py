from tkinter import *
from tkinter import ttk
from config import *
# Cores
bg_root = "#252F44"
bg_head = "#EEEEEE"
bg_body = "#5C5470"
bg_button = "#F3E9DD"
bg_button_rigth = "#FFC26F"
bg_font_button_rigth = "#F5F5F5"


def calculadora():
    root = Tk()
    root.title("Calculadora")
    root.geometry("235x310")
    root.resizable(False, False)
    root.config(bg=bg_root)

    # Criando os frames de fundo
    frame_head = Frame(root, width=235, height=50, bg=bg_head)
    frame_head.grid(row=0, column=0)

    frame_body = Frame(root, width=235, height=268, bg=bg_body)
    frame_body.grid(row=1, column=0)

    # Criando Label
    value = StringVar()
    result_box = Label(frame_head, textvariable=value, width=13, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT,fg='#000000', font=('Arial 20'), bg=bg_head)
    result_box.place(x=0, y=0)

    # Criando os botões
    # Row 1
    button_clear = Button(frame_body,command=lambda:limpar_campo(value), text="C", width=11, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_clear.place(x=0, y=0)
    button_percent = Button(frame_body,command=lambda:exibir_valor(value, '%'), text="%", width=5, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_percent.place(x=119, y=0)
    button_division = Button(frame_body,command=lambda:exibir_valor(value, '/'), text="/", width=5, height=2, bg=bg_button_rigth, fg=bg_font_button_rigth, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_division.place(x=178, y=0)
    
    # Row 2
    button_seven = Button(frame_body,command=lambda:exibir_valor(value, '7'), text="7", width=5, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_seven.place(x=1, y=52)
    button_eight = Button(frame_body,command=lambda:exibir_valor(value, '8'), text="8", width=5, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_eight.place(x=60, y=52)
    button_nine = Button(frame_body,command=lambda:exibir_valor(value, '9'), text="9", width=5, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_nine.place(x=119, y=52)
    button_multiplication = Button(frame_body,command=lambda:exibir_valor(value, '*'), text="*", width=5, height=2, bg=bg_button_rigth, fg=bg_font_button_rigth, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_multiplication.place(x=178, y=52)

    # row 3
    button_four = Button(frame_body,command=lambda:exibir_valor(value, '4'), text="4", width=5, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_four.place(x=1, y=104)
    button_five = Button(frame_body,command=lambda:exibir_valor(value, '5'), text="5", width=5, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_five.place(x=60, y=104)
    button_six = Button(frame_body,command=lambda:exibir_valor(value, '6'), text="6", width=5, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_six.place(x=119, y=104)
    button_subtraction = Button(frame_body,command=lambda:exibir_valor(value, '-'), text="-", width=5, height=2, bg=bg_button_rigth, fg=bg_font_button_rigth, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_subtraction.place(x=178, y=104)

    # row 4
    button_one = Button(frame_body,command=lambda:exibir_valor(value, '1'), text="1", width=5, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_one.place(x=1, y=156)
    button_two = Button(frame_body,command=lambda:exibir_valor(value, '2'), text="2", width=5, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_two.place(x=60, y=156)
    button_three = Button(frame_body,command=lambda:exibir_valor(value, '3'), text="3", width=5, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_three.place(x=119, y=156)
    button_sum = Button(frame_body,command=lambda:exibir_valor(value, '+'), text="+", width=5, height=2, bg=bg_button_rigth, fg=bg_font_button_rigth, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_sum.place(x=178, y=156)

    # row 5
    button_zero = Button(frame_body,command=lambda:exibir_valor(value, '0'), text="0", width=17, height=2, bg=bg_button, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_zero.place(x=-1, y=208)
    button_result = Button(frame_body, command=lambda:resultado(value), text="=", width=5, height=2, bg=bg_button_rigth, fg=bg_font_button_rigth, font=('Arial 13 bold'),relief=RAISED, overrelief=RIDGE)
    button_result.place(x=178, y=208)

    root.mainloop()

calculadora()