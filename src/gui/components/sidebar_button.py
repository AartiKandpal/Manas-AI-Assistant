import customtkinter as ctk

from gui.theme import *


class SidebarButton(ctk.CTkButton):

    def __init__(self, parent, text, icon, command):

        super().__init__(
            parent,

            text=f"{icon}   {text}",

            command=command,

            anchor="w",

            height=52,

            corner_radius=16,

            fg_color="#000000",

            hover_color=HOVER,

            text_color=TEXT,

            font=("Segoe UI", 15, "bold"),

            border_width=1,

            border_color="#000000"
        )

    def activate(self):

        self.configure(

            fg_color=PRIMARY,

            hover_color=PRIMARY,

            text_color="white",

            border_color="#7BE495"
        )

    def deactivate(self):

        self.configure(

            fg_color=CARD,

            hover_color="#CBEFC5",

            text_color=TEXT,

        )