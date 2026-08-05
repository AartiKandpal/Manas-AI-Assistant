import customtkinter as ctk


class MicWidget(ctk.CTkButton):

    def __init__(self, parent, command):

        super().__init__(
            parent,
            text="🎤",
            width=70,
            height=70,
            corner_radius=35,
            font=("Segoe UI Emoji", 28),
            fg_color="#7C5CFF",
            hover_color="#9575FF",
            command=command
        )