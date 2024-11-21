from view_staff_page import ViewStaffPage
from customer_menu_page import CustomerMenuPage
from treeview_page import TreeviewPage
from tkinter import *
from functools import partial

class ActionsPage(TreeviewPage):
    def __init__(self, database):
        columns = [
            "Action",
            "Description"
        ]

        TreeviewPage.__init__(self, database, "Actions Page", columns)

    def render(self):
        self.__render_treeview()
        self.__render_logout()

    def __render_treeview(self):
        self._treeview.insert("", "end", values=("View Staff", "BLABLABLA"))
        self._treeview.insert("", "end", values=("View Menu", "BLABLABLA"))
        self._treeview.bind("<Double-1>", self.__execute_action)
        self._treeview.grid(row=0, column=0)

    def __execute_action(self, event):
        if self.__get_submenu() == "View Staff":
            self._window.destroy()
            ViewStaffPage(self._database).render()
            return

        if self.__get_submenu() == "View Menu":
            self._window.destroy()
            CustomerMenuPage(self._database).render()
            return

    def __get_submenu(self):
        item = self._treeview.selection()[0]
        return self._treeview.item(item, "values")[0]

    def __render_logout(self):
        command_logout = partial(self.__logout)
        Button(self._window, text="Logout", command=command_logout).grid(row=1, column=0)

    def __logout(self):
        self._window.destroy()