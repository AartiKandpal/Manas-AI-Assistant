import customtkinter as ctk

from audio.listener import Listener
from gui.backend import Backend
from gui.components.status_label import StatusLabel
from gui.theme import *


class ChatPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color=BACKGROUND)

        self.backend = Backend()
        self.listener = Listener()

        self.is_processing = False

        # =========================
        # Header
        # =========================

        top = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        top.pack(fill="x", padx=30, pady=(20, 10))

        title = ctk.CTkLabel(
            top,
            text="💬 Chat with Manas",
            font=("Segoe UI", 30, "bold")
        )
        title.pack(anchor="w")

        self.status = StatusLabel(top)
        self.status.pack(anchor="w", pady=(6, 0))

        # =========================
        # Chat Box
        # =========================

        self.chat = ctk.CTkTextbox(
            self,
            fg_color=CARD,
            corner_radius=18,
            font=("Segoe UI", 15),
            wrap="word"
        )

        self.chat.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(10, 18)
        )

        self.chat.tag_config(
            "user",
            foreground=PRIMARY,
        )

        self.chat.tag_config(
            "bot",
            foreground=PRIMARY,
        )

        # 👇 Message text is now BLACK
        self.chat.tag_config(
            "text",
            foreground="black",
        )

        self.chat.insert(
            "end",
            "🤖 Welcome to Manas!\n\n",
            "bot"
        )

        # =========================
        # Bottom Bar
        # =========================

        bottom = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        bottom.pack(
            fill="x",
            padx=30,
            pady=(0, 25)
        )

        self.entry = ctk.CTkEntry(
            bottom,
            height=50,
            corner_radius=25,
            font=("Segoe UI", 15),
            placeholder_text="Ask Manas anything..."
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 12)
        )

        self.entry.bind("<Return>", self.send)

        voice = ctk.CTkButton(
            bottom,
            text="🎤",
            width=50,
            height=50,
            corner_radius=25,
            command=self.voice_chat
        )

        voice.pack(side="right", padx=(0, 10))

        send = ctk.CTkButton(
            bottom,
            text="➜",
            width=50,
            height=50,
            corner_radius=25,
            command=self.send
        )

        send.pack(side="right")

    # =================================================

    def add_user(self, text):

        self.chat.insert("end", "\n🧑 You\n", "user")
        self.chat.insert("end", text + "\n\n", "text")
        self.chat.see("end")

    def add_bot(self, text):

        self.chat.insert("end", "🤖 Manas\n", "bot")
        self.chat.insert("end", text + "\n\n", "text")
        self.chat.see("end")

    # =================================================

    def send(self, event=None):

        if self.is_processing:
            return

        prompt = self.entry.get().strip()

        if not prompt:
            return

        self.is_processing = True

        self.add_user(prompt)

        self.entry.delete(0, "end")

        self.status.thinking()
        self.update()

        try:

            reply = self.backend.ask(prompt)

            self.status.speaking()

            self.add_bot(reply)

        except Exception as e:

            self.add_bot(str(e))

        finally:

            self.is_processing = False
            self.after(1200, self.status.idle)

    # =================================================

    def voice_chat(self):

        if self.is_processing:
            return

        self.is_processing = True

        self.status.listening()
        self.update()

        try:

            text = self.listener.listen()

            if not text:
                return

            self.add_user(text)

            self.status.thinking()
            self.update()

            reply = self.backend.ask(text)

            self.status.speaking()

            self.add_bot(reply)

        except Exception as e:

            self.add_bot(str(e))

        finally:

            self.is_processing = False
            self.after(1200, self.status.idle)