from page import Page

class ViewStaffPage(Page):
    def __init__(self, database):
        columns = [
            "Forename",
            "Surname"
            "DOB",
            "Role",
            "Employed on"
        ]

        Page.__init__(self, database, "view staff", columns)

    def render(self):
        self._treeview.pack(fill="x")
        self._window.mainloop()