import tkinter
import sqlite3
from tkinter import ttk

window = tkinter.Tk()
window.title("4kitsw10 COM519")

treeview = ttk.Treeview(columns=("size", "lastmod"))
treeview.heading("#0", text="Name")
treeview.heading("size", text="RSP")
treeview.heading("lastmod", text="Calories")

connection_obj = sqlite3.connect("4kitsw10_COM519_database")
cursor = connection_obj.cursor()

cursor.execute(f"SELECT * FROM Customer_Facing_Menu")

for row in cursor.fetchall():
    treeview.insert(
        "",
        tkinter.END,
        text=row[1],
        values=(row[2], row[3])
    )

treeview.pack()
window.mainloop()