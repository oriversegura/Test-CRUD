import tkinter as tk

from tkinter import *
from tkinter import mainloop, ttk
from tkinter import messagebox


def main():
    class FormClients:
        def Form():
            try:
                base = Tk()
                base.geometry("1200x300")
                base.title("Test CRUD")

                groupBox = LabelFrame(base, text="Employee Data", padx=5, pady=5)
                groupBox.grid(row=0, column=0, padx=10, pady=10)

                labelID = Label(
                    groupBox, text="ID:", width=13, font=("Arial", 12)
                ).grid(row=0, column=0)
                textBoxID = Entry(groupBox).grid(row=0, column=1)

                base.mainloop()

            except ValueError as error:
                print(f"Error to show interface {error}")

        Form()


if __name__ == "__main__":
    main()
