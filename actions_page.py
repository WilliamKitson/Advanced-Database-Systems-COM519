from treeview_page import TreeviewPage

class ActionsPage(TreeviewPage):
    def __init__(self, database):
        columns = [
            "Action"
        ]

        TreeviewPage.__init__(self, database, "Actions Page", columns)

    def render(self):
        self._treeview.grid(row=0, column=0)