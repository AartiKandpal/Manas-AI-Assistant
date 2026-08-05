import customtkinter as ctk


class StatusLabel(ctk.CTkLabel):

    def __init__(self, parent):
        super().__init__(
            parent,
            text="⚫ Idle",
            font=("Segoe UI", 16, "bold"),
            text_color="#A9A9A9"
        )

    def idle(self):
        self.configure(text="⚫ Idle", text_color="#A9A9A9")

    def listening(self):
        self.configure(text="🎤 Listening...", text_color="#00BFFF")

    def thinking(self):
        self.configure(text="🧠 Thinking...", text_color="#FFD54F")

    def speaking(self):
        self.configure(text="🗣 Speaking...", text_color="#7C5CFF")