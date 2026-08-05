import customtkinter as ctk

from gui.theme import *
from gui.components.sidebar_button import SidebarButton


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, callback):

        super().__init__(
            parent,
            width=260,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.pack_propagate(False)

        # ==========================
        # LOGO
        # ==========================

        logo_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        logo_frame.pack(pady=(30, 18))

        ctk.CTkLabel(
            logo_frame,
            text="🧠",
            font=("Segoe UI Emoji", 42)
        ).pack()

        ctk.CTkLabel(
            logo_frame,
            text="MANAS",
            font=("Segoe UI", 30, "bold"),
            text_color=TEXT
        ).pack()

        ctk.CTkLabel(
            logo_frame,
            text="Offline AI Assistant",
            font=("Segoe UI", 13),
            text_color=SUBTEXT
        ).pack()

        # ==========================
        # VERSION
        # ==========================

        version = ctk.CTkLabel(
            self,
            text="v1.0 Beta",
            font=("Segoe UI", 11),
            text_color=PRIMARY
        )

        version.pack(pady=(0, 25))

        # ==========================
        # NAVIGATION
        # ==========================

        self.buttons = {}

        pages = [
            ("🏠", "Home"),
            ("💬", "Chat"),
            ("⚡", "Commands"),
            ("🕘", "History"),
            ("ℹ", "About")
        ]

        for icon, page in pages:

            btn = SidebarButton(
                self,
                text=page,
                icon=icon,
                command=lambda p=page: self.change(p, callback)
            )

            btn.pack(
                fill="x",
                padx=16,
                pady=5
            )

            self.buttons[page] = btn

        # Push footer to bottom
        spacer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        spacer.pack(expand=True, fill="both")

        # ==========================
        # FOOTER
        # ==========================

        footer = ctk.CTkFrame(
            self,
            fg_color=CARD
        )

        footer.pack(
            side="bottom",
            pady=25
        )

        ctk.CTkLabel(
            footer,
            text="Local • Private",
            font=("Segoe UI", 12),
            text_color=SUBTEXT
        ).pack()

        ctk.CTkLabel(
            footer,
            text="Powered by Ollama",
            font=("Segoe UI", 11),
            text_color="#666666"
        ).pack()

    def change(self, page, callback):

        for button in self.buttons.values():
            button.deactivate()

        self.buttons[page].activate()

        callback(page)