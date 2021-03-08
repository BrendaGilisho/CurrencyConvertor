# Authors : Brenda

from tkinter import *
import tkinter as tk
from tkinter import ttk
import re
from real_time_converter import *

class App(Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.currency_converter = RealTimeCurrencyConverter()

        # Label
        self.intro_label = Label(self, text='WELCOME:Simple Currency Convertor!', anchor="center", fg='blue', relief=tk.RAISED,
                                 borderwidth=5)
        self.intro_label.config(font=('Courier', 15, 'bold'))
        self.config(bg='lightgrey')

        self.intro_label.place(x=10, y=5)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text='',fg='black', bg='white', relief=tk.RIDGE,
                                                  justify=tk.CENTER, width=17, borderwidth=3)

        # base dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("USD")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("RWF")  # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)

        print (type(self.currency_converter.response["rates"]))

        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.currency_converter.response["rates"].keys()), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER)

        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.response["rates"].keys()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        # self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_label.place(x=346, y=150)
        #tk.Button(frame, text="Convert", command=convert)
        # Convert button
        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=225, y=135)

    def perform(self):
        amount = float(self.amount_field.get())

        from_curr = self.from_currency_variable.get()
        from_curr = self.currency_converter.response["rates"][from_curr]

        to_curr = self.to_currency_variable.get()
        to_curr = self.currency_converter.response["rates"][to_curr]


        converted_amount = amount / from_curr
        final_converted_amnt = converted_amount * to_curr

        final_converted_amnt = round(final_converted_amnt, 2)

        self.converted_amount_field_label.config(text=str(final_converted_amnt))

    def restrictNumberOnly(self, action, string):
         regex = re.compile(r'[0-9,]*?(\.)?[0-9,]*$')
         result = regex.match(string)
         return (string == "" or (string.count('.') <= 1 and result is not None))

if __name__ == '__main__':
    #window = Tk()
    mywin = App()
    mywin.title('Currency Convertor: Brenda')
    mywin.geometry("600x300+10+10")
    mywin.mainloop()




