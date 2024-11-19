from page import Page

class ViewStaffPage(Page):
    def __init__(self, database):
        columns = [
            "Forename",
            "Surname",
            "Age",
            "Tenure",
            "Role"
        ]

        Page.__init__(self, database, "view staff", columns)

    def render(self):
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

        self._treeview.pack(fill="x")
        self._window.mainloop()