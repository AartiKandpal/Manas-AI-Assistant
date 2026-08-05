import customtkinter as ctk

from gui.theme import *


class AboutPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color=BACKGROUND)

        scroll = ctk.CTkScrollableFrame(
            self,
            fg_color=BACKGROUND
        )
        scroll.pack(fill="both", expand=True, padx=20, pady=20)

        # ==================================================
        # HEADER
        # ==================================================

        header = ctk.CTkFrame(
            scroll,
            fg_color="transparent"
        )
        header.pack(fill="x", pady=(0, 18))

        ctk.CTkLabel(
            header,
            text="MANAS AI",
            font=("Segoe UI", 30, "bold"),
            text_color=TEXT
        ).pack(anchor="w")

        ctk.CTkLabel(
            header,
            text="Private • Offline • Intelligent",
            font=("Segoe UI", 14),
            text_color=SUBTEXT
        ).pack(anchor="w", pady=(2, 10))

        description = (
            "Manas AI is a fully local desktop assistant built using Python and Ollama. "
            "It understands natural voice commands, answers questions, automates desktop "
            "tasks and remembers conversations while keeping all processing completely "
            "offline, ensuring your data remains private on your own device."
        )

        ctk.CTkLabel(
            header,
            text=description,
            justify="left",
            wraplength=900,
            font=("Segoe UI", 14),
            text_color=TEXT
        ).pack(anchor="w")

        # ==================================================
        # CAPABILITIES
        # ==================================================

        cap = ctk.CTkFrame(
            scroll,
            fg_color=CARD,
            corner_radius=18
        )
        cap.pack(fill="x", pady=15)

        ctk.CTkLabel(
            cap,
            text="⚡ Capabilities",
            font=("Segoe UI", 18, "bold"),
            text_color=TEXT
        ).pack(anchor="w", padx=20, pady=(15, 15))

        body = ctk.CTkFrame(
            cap,
            fg_color="transparent"
        )
        body.pack(fill="x", padx=30, pady=(0, 18))

        left = ctk.CTkFrame(body, fg_color="transparent")
        left.pack(side="left", expand=True, anchor="n")

        right = ctk.CTkFrame(body, fg_color="transparent")
        right.pack(side="right", expand=True, anchor="n")

        left_features = [
            ("🧠", "Local LLM (Ollama)", "Powered by Qwen2.5 model"),
            ("🎤", "Speech Recognition", "Faster Whisper for accurate STT"),
            ("🔊", "Natural Voice Output", "Edge-TTS for lifelike responses"),
            ("💻", "Desktop Automation", "Open apps and tools with ease"),
        ]

        right_features = [
            ("🌐", "Browser Control", "Search, open and automate"),
            ("🗂", "Memory System", "Remembers conversations"),
            ("🔒", "Privacy First", "Everything stays on your device"),
            ("⚡", "Fast Response", "Optimized local execution"),
        ]

        for icon, title, sub in left_features:

            row = ctk.CTkFrame(left, fg_color="transparent")
            row.pack(anchor="w", pady=10)

            ctk.CTkLabel(
                row,
                text=icon,
                font=("Segoe UI Emoji", 24)
            ).pack(side="left", padx=(0, 12))

            txt = ctk.CTkFrame(row, fg_color="transparent")
            txt.pack(side="left")

            ctk.CTkLabel(
                txt,
                text=title,
                font=("Segoe UI", 15, "bold"),
                text_color=TEXT
            ).pack(anchor="w")

            ctk.CTkLabel(
                txt,
                text=sub,
                font=("Segoe UI", 13),
                text_color=SUBTEXT
            ).pack(anchor="w")

        for icon, title, sub in right_features:

            row = ctk.CTkFrame(right, fg_color="transparent")
            row.pack(anchor="w", pady=10)

            ctk.CTkLabel(
                row,
                text=icon,
                font=("Segoe UI Emoji", 24)
            ).pack(side="left", padx=(0, 12))

            txt = ctk.CTkFrame(row, fg_color="transparent")
            txt.pack(side="left")

            ctk.CTkLabel(
                txt,
                text=title,
                font=("Segoe UI", 15, "bold"),
                text_color=TEXT
            ).pack(anchor="w")

            ctk.CTkLabel(
                txt,
                text=sub,
                font=("Segoe UI", 13),
                text_color=SUBTEXT
            ).pack(anchor="w")
                    # ==================================================
        # TECH STACK
        # ==================================================

        tech = ctk.CTkFrame(
            scroll,
            fg_color=CARD,
            corner_radius=18
        )
        tech.pack(fill="x", pady=12)

        ctk.CTkLabel(
            tech,
            text="🛠 Tech Stack",
            font=("Segoe UI", 18, "bold"),
            text_color=TEXT
        ).pack(anchor="w", padx=20, pady=(15, 8))

        ctk.CTkLabel(
            tech,
            text=(
                "Python  •  Ollama  •  Qwen2.5  •  Faster Whisper"
                "Edge-TTS   •  PyAudio  •  CustomTkinter"
            ),
            justify="left",
            font=("Segoe UI", 14),
            text_color=TEXT
        ).pack(anchor="w", padx=20, pady=(0, 15))

        # ==================================================
        # WORKFLOW
        # ==================================================

        workflow = ctk.CTkFrame(
            scroll,
            fg_color=CARD,
            corner_radius=18
        )
        workflow.pack(fill="x", pady=12)

        ctk.CTkLabel(
            workflow,
            text="🔄 Workflow",
            font=("Segoe UI", 18, "bold"),
            text_color=TEXT
        ).pack(anchor="w", padx=20, pady=(15, 12))

        flow = ctk.CTkFrame(
            workflow,
            fg_color="transparent"
        )
        flow.pack(pady=(0, 18))

        steps = [
            "🎤 Input",
            "📝 Whisper",
            "🧠 Ollama",
            "⚙ Execute",
            "🔊 Reply"
        ]

        for i, step in enumerate(steps):

            box = ctk.CTkFrame(
                flow,
                fg_color=BACKGROUND,
                corner_radius=10,
                width=120,
                height=52
            )
            box.grid(row=0, column=i * 2, padx=4)
            box.pack_propagate(False)

            ctk.CTkLabel(
                box,
                text=step,
                font=("Segoe UI", 13, "bold"),
                text_color=TEXT
            ).pack(expand=True)

            if i < len(steps) - 1:

                ctk.CTkLabel(
                    flow,
                    text="➜",
                    font=("Segoe UI", 18, "bold"),
                    text_color=PRIMARY
                ).grid(row=0, column=i * 2 + 1, padx=3)

        # ==================================================
        # FOOTER
        # ==================================================

        footer = ctk.CTkLabel(
            scroll,
            text=(
                "MANAS AI v1.0 \n"
                "Developed by Aarti Kandpal\n"
                "Built with Python • Powered by Ollama"
            ),
            justify="center",
            font=("Segoe UI", 13),
            text_color=SUBTEXT
        )

        footer.pack(pady=(18, 10))