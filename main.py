import tkinter
from customer_menu_page import CustomerMenuPage

window = tkinter.Tk()
window.title("4kitsw10 COM519")
window.geometry("1280x720")
CustomerMenuPage(window).render()
window.mainloop()