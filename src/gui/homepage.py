import customtkinter as ctk

from gui.theme import *
from gui.components.animated_ring import AnimatedRing


class HomePage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=BACKGROUND
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        container.pack(expand=True)

        # ==========================
        # APP TITLE
        # ==========================

        title = ctk.CTkLabel(
            container,
            text="MANAS",
            font=("Segoe UI", 42, "bold"),
            text_color=TEXT
        )
        title.pack(pady=(10, 2))

        subtitle = ctk.CTkLabel(
            container,
            text="Your Personal Offline AI Assistant",
            font=("Segoe UI", 16),
            text_color=SUBTEXT
        )
        subtitle.pack()

        # ==========================
        # Animated Ring
        # ==========================

        ring = AnimatedRing(container)
        ring.pack(pady=(35, 25))

        # ==========================
        # Microphone
        # ==========================

        mic = ctk.CTkFrame(
            ring,
            width=135,
            height=135,
            corner_radius=70,
            fg_color=PRIMARY
        )

        mic.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        mic_label = ctk.CTkLabel(
            mic,
            text="🎤",
            font=("Segoe UI Emoji", 56)
        )

        mic_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ==========================
        # STATUS
        # ==========================

       

        self.subtitle = ctk.CTkLabel(
            container,
            text='Say "Hey Manas" or start typing below',
            font=("Segoe UI", 15),
            text_color=SUBTEXT
        )
        self.subtitle.pack()

        # ==========================
        # QUICK ACTIONS
        # ==========================

        quick = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )
        quick.pack(pady=35)

        actions = [
            "💬 Chat",
            "🌐 Search",
            "📝 Notes",
            "⚙ Automation"
        ]

        for text in actions:

            btn = ctk.CTkButton(
                quick,
                text=text,
                width=130,
                height=42,
                corner_radius=18,
                fg_color=CARD,
                hover_color=PRIMARY,
                text_color=TEXT,
                font=("Segoe UI", 14)
            )

            btn.pack(
                side="left",
                padx=8
            )

        # ==========================
        # INPUT BAR
        # ==========================

        bottom = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        bottom.pack(
            side="bottom",
            fill="x",
            padx=70,
            pady=35
        )

        self.entry = ctk.CTkEntry(
            bottom,
            placeholder_text="Ask Manas anything...",
            height=56,
            corner_radius=30,
            font=("Segoe UI", 16)
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 15)
        )

        send = ctk.CTkButton(
            bottom,
            text="➜",
            width=56,
            height=56,
            corner_radius=28,
            fg_color=PRIMARY,
            hover_color="#4338CA",
            font=("Segoe UI", 22, "bold")
        )

        send.pack(side="right")

        # ==========================
        # FOOTER
        # ==========================

        footer = ctk.CTkLabel(
            self,
            text="Local • Private • Powered by Ollama",
            text_color=SUBTEXT,
            font=("Segoe UI", 13)
        )

        footer.pack(side="bottom", pady=(0, 12))

    # =====================================================
    # HOME STATUS METHODS
    # =====================================================

    def set_ready(self):

        self.status.configure(
            text="✅ Ready"
        )

        self.subtitle.configure(
            text='Say "Hey Manas" or start typing below'
        )

    def set_listening(self):

        self.status.configure(
            text="🎤 Listening..."
        )

        self.subtitle.configure(
            text="Listening to you..."
        )

    def set_thinking(self):

        self.status.configure(
            text="🧠 Thinking..."
        )

        self.subtitle.configure(
            text="Understanding your request..."
        )

    def set_speaking(self):

        self.status.configure(
            text="🗣 Speaking..."
        )

        self.subtitle.configure(
            text="Generating response..."
        )