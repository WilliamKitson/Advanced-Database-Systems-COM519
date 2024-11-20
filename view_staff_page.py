from tkinter import *
from treeview_page import TreeviewPage

class ViewStaffPage(TreeviewPage):
    def __init__(self, database):
        columns = [
            "Forename",
            "Surname",
            "Age",
            "Tenure",
            "Role"
        ]

        TreeviewPage.__init__(
            self,
            database,
            "view staff",
            columns
        )

    def render(self):
        self.__render_treeview()
        self.__render_add()
        self._window.mainloop()

    def __render_treeview(self):
        self._cursor.execute(
            "SELECT * "
            "FROM View_Team_Members"
        )

        for row in self._cursor.fetchall():
            self._treeview.insert("", "end", values=(
                row[0],
                row[1],
                f"{row[2]} years",
                f"{row[3]} years",
                row[4]
            ))

        self._treeview.grid(row=0, column=0)

    def __render_add(self):
        Button(self._window, text="Add Staff").grid(row=1, column=0)