import customtkinter as ctk

from gui.theme import *
from gui.sidebar import Sidebar
from gui.homepage import HomePage
from gui.chat import ChatPage
from gui.commands import CommandsPage
from gui.about import AboutPage


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class ManasGUI(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Manas AI Assistant")
        self.geometry("1450x850")
        self.minsize(1250, 720)

        self.configure(fg_color=BACKGROUND)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = Sidebar(
            self,
            self.change_page
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # Main Container
        self.container = ctk.CTkFrame(
            self,
            fg_color=BACKGROUND,
            corner_radius=0
        )

        self.container.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Pages
        self.pages = {
            "Home": HomePage(self.container),
            "Chat": ChatPage(self.container),
            "Commands": CommandsPage(self.container),
            "About": AboutPage(self.container)
        }

        for page in self.pages.values():
            page.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

        # Default page
        self.sidebar.change("Home",self.change_page)

    def change_page(self, page):

        self.pages[page].tkraise()

        

def main():

    app = ManasGUI()
    app.mainloop()


if __name__ == "__main__":
    main()