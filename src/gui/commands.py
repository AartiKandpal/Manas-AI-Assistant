import customtkinter as ctk

from gui.theme import *


class CommandsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=BACKGROUND
        )

        title = ctk.CTkLabel(
            self,
            text="Quick Commands",
            font=("Segoe UI", 30, "bold"),
            text_color=TEXT
        )

        title.pack(anchor="w", padx=35, pady=(25, 20))

        grid = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        grid.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        commands = [

            ("🌐", "Chrome", "Open Chrome"),
            ("💻", "VS Code", "Open VS Code"),
            ("🧮", "Calculator", "Open Calculator"),

            ("📝", "Notepad", "Open Notepad"),
            ("🔍", "Google", "Google Search"),
            ("▶", "YouTube", "YouTube Search"),

            ("📄", "Create File", "Create File"),
            ("🗑", "Delete File", "Delete File"),
            ("🧠", "Memory", "Memory"),

            ("🗺", "Maps", "Maps"),
        ]

        cols = 3

        for i in range(cols):
            grid.grid_columnconfigure(i, weight=1)

        row = 0
        col = 0

        for icon, title, subtitle in commands:

            card = ctk.CTkFrame(
                grid,
                fg_color=CARD,
                corner_radius=18,
                height=140
            )

            card.grid(
                row=row,
                column=col,
                padx=12,
                pady=12,
                sticky="nsew"
            )

            ctk.CTkLabel(
                card,
                text=icon,
                font=("Segoe UI Emoji", 34)
            ).pack(pady=(18, 8))

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 18, "bold"),
                text_color=TEXT
            ).pack()

            ctk.CTkLabel(
                card,
                text=subtitle,
                font=("Segoe UI", 13),
                text_color=SUBTEXT
            ).pack(pady=(2, 15))

            col += 1

            if col == cols:
                col = 0
                row += 1